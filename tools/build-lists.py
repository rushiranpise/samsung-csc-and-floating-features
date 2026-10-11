"""Build the feature-gate documentation from every source gathered.

Sources, all recorded per entry so the lists can be traced back:
  scan     - the keys read by the system apps on a One UI 8 device (SM-S938U1)
  koo      - the carrier CSC file in y6yuan/SamsungKOO2CHC
  mzdyl    - the config tables in Mzdyl/OneUI_CSC_Features
  el0xren  - the floating feature and CSC lists in el0xren/Samsung_Additional_Features
  device   - the values this device's own carrier and floating files hold
"""
import json
import pathlib
import re
from collections import defaultdict

TMP = pathlib.Path(r"C:\Users\rushi\Downloads\freebuff\tmp")
REFS = TMP / "refs"
OUT = TMP / "gates-repo"
for sub in ("", "data", "tools"):
    (OUT / sub).mkdir(parents=True, exist_ok=True)

CSC = "CscFeature_"
FF = "SEC_FLOATING_FEATURE_"

# What has been checked on a real device, and how. Everything else is untested, which is worth
# saying plainly: a key doing nothing is not evidence that the key is wrong, since a feature read by
# native code that parses the floating feature file itself never sees an answer given here.
VERIFIED = {
    "SEC_FLOATING_FEATURE_BATTERY_SUPPORT_BSOH_SETTINGS":
        "tested on an SM-S938U1 with the gate on and then off: About phone > Battery information "
        "shows the same battery health, cycle count and capacity rows either way, so this key does "
        "not control them",
    "CscFeature_Setting_EnableHwVersionDisplay":
        "tested on an SM-S938U1: no hardware version row appears in About phone. The value was "
        "entered as 'true' where the references give 'TRUE', so a retry with the reference value is "
        "the next thing to try",
}

# Codes read straight out of the source above rather than guessed:
# the app that owns a key is the most specific one that reads it.
CATEGORY_ORDER = [
    "Camera", "Gallery", "Dialer", "Contacts", "ContactsProvider", "VideoPlayer",
    "VideoEditor", "Browser", "Weather", "AOD", "SmartCapture", "SoundAlive",
    "AdaptSound", "Bixby", "DynLockscreen", "BlueLightFilter", "VTCamera", "CallBG",
    "CalendarProvider", "Telephony", "SecSettingsIntel", "SecSettings",
    "services.jar", "framework.jar",
]

entries = {}


def add(key, source, category=None, description=None, value=None):
    key = key.strip()
    if not key.startswith((CSC, FF)):
        return
    e = entries.setdefault(
        key,
        {"key": key, "table": "csc" if key.startswith(CSC) else "floating",
         "category": None, "description": None, "description_source": None,
         "value": None, "values": {}, "from": [], "read_by": []},
    )
    if source not in e["from"]:
        e["from"].append(source)
    if category and source == "scan" and category not in e["read_by"]:
        e["read_by"].append(category)
    # Some lists close a tag without a slash, and a key mentioned without a value has none to record.
    value = (value or "").strip() or None
    if value is not None:
        e["values"][source] = value
    if description and not e["description"]:
        e["description"] = description
        e["description_source"] = source


def words(text):
    text = text.replace("_", " ")
    return re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", text).strip()


VERBS = {
    "Support": "adds", "Enable": "enables", "Disable": "turns off", "Config": "sets",
    "Use": "uses", "Set": "sets", "Remove": "removes", "Show": "shows", "Hide": "hides",
    "Allow": "allows", "Block": "blocks", "Change": "changes", "Force": "forces",
    "Auto": "auto", "Always": "always",
}


def area_of(key):
    """The area a key belongs to, which is the word between the table and the feature."""
    body = key[len(CSC):] if key.startswith(CSC) else key[len(FF):]
    seg = body.split("_")[0]
    # Short upper case words are acronyms and read better untouched (RIL, GMS, AOD).
    return seg if seg.isupper() and len(seg) <= 4 else words(seg.title() if seg.isupper() else seg)


def derived(key):
    """A short gloss taken from the key name, used where no reference describes it."""
    body = key[len(CSC):] if key.startswith(CSC) else key[len(FF):]
    area, _, rest = body.partition("_")
    area = area_of(key)
    if not rest:
        return area
    for prefix, verb in VERBS.items():
        if rest.lower().startswith(prefix.lower()):
            tail = words(rest)[len(prefix):].strip()
            return f"{area}: {verb} {tail.lower()}" if tail else f"{area}: {verb}"
    return f"{area}: {words(rest).lower()}"


# --- 1. the keys the system apps read, with the app each came from
for line in (TMP / "apkkeys.tsv").read_text(encoding="utf-8").splitlines():
    if "\t" not in line:
        continue
    app, key = line.split("\t", 1)
    add(key, "scan", category=app.strip())

# --- 2. the carrier CSC file from SamsungKOO2CHC
for name in ("cscfeature.xml", "cscfeature_network.xml"):
    f = REFS / "SamsungKOO2CHC" / "optics_new/configs/carriers/single/KOO/conf" / name
    if f.exists():
        for key, value in re.findall(r"<(CscFeature_[A-Za-z0-9_]+)>([^<]*)</",
                                     f.read_text(encoding="utf-8")):
            add(key, "koo", value=value)

# The config tables also carry the value each key is meant to take, which is the most useful thing
# to publish next to a key: it is what the feature is switched on with.
for config in ("csc.json", "ff.json"):
    f = REFS / "OneUI_CSC_Features/module_files/configs" / config
    if f.exists():
        for row in json.loads(f.read_text(encoding="utf-8")):
            add(row["key"], "mzdyl", value=row.get("value"))

# --- 3. the config tables in Mzdyl/OneUI_CSC_Features, whose notes are Chinese
MZDYL = {
    "CscFeature_Calendar_EnableLocalHolidayDisplay": "adds local public holidays to Calendar",
    "CscFeature_Calendar_EnableLunar": "adds lunar dates to Calendar",
    "CscFeature_Weather_ConfigCpType": "changes the weather provider",
    "CscFeature_Setting_SupportRealTimeNetworkSpeed": "adds the network speed setting",
    "CscFeature_SPen_ConfigDefTranslatorSolution": "changes the S Pen translation service",
    "CscFeature_VoiceCall_ConfigRecording": "allows voice call recording",
    "CscFeature_Camera_ShutterSoundMenu": "shows the camera shutter sound menu (no effect on Android 14 and later)",
    "CscFeature_Contact_EnableBPMFSortList": "removes the Bopomofo contact sort list",
    "CscFeature_Contact_EnableStrokeSortList": "removes the stroke contact sort list",
    "CscFeature_SystemUI_ConfigRecentDefaultLockList": "removes the default list of locked recents apps",
    "CscFeature_SmartManager_ConfigSubFeatures": "picks which Smart Manager features exist",
    "CscFeature_Setting_EnableMenuBlockCallMsg": "adds the block calls and messages menu",
    "CscFeature_Contact_ConfigForYellowPage": "adds yellow pages",
    "CscFeature_Audio_SupportSafeMediaVolumeDialog": "shows the safe media volume warning",
    "CscFeature_Common_ConfigSvcProviderForUnknownNumber": "removes the unknown number lookup provider",
    "CscFeature_RIL_CallerIdMatchingDigit": "sets how many digits caller ID matches on",
    "CscFeature_Calculator_ConfigConverter": "sets which units the Calculator converts",
    "CscFeature_Clock_ConfigLocalTimerPreset": "sets the local timer presets",
    "CscFeature_Clock_EnableAutoPowerOnOffMenu": "adds the auto power on and off menu",
    "CscFeature_Clock_SupportAlarmOptionMenuForWorkingDay": "adds the working day alarm option",
    "CscFeature_Contact_ConfigTelNumType": "sets the phone number type used in Contacts",
    "CscFeature_Contact_EnableMultiplePinyinSearch": "adds pinyin search to Contacts",
    "CscFeature_Contact_EnablePuzzySearch": "adds fuzzy search to Contacts",
    "CscFeature_Contact_UseUniNameField": "uses one unified name field in Contacts",
    "CscFeature_Message_EnableCpm": "enables CPM messaging",
    "CscFeature_Message_SupportBotThreadsMerge": "merges chat bot threads in Messages",
    "CscFeature_Message_EnablePhoneNumberFormattingInMsg": "formats phone numbers inside messages",
    "CscFeature_Setting_EnableHwVersionDisplay": "shows the hardware version in Settings",
    "CscFeature_Setting_SupportPreInstallerShowPreloadAppList": "shows the list of preinstalled apps",
    "CscFeature_VoiceCall_ConfigOpStyleForImsFunction": "picks which IMS call features exist",
    "CscFeature_VoiceCall_ConfigOpStyleForSpamCall": "sets how spam calls are handled",
    "CscFeature_VoiceCall_SupportCrtCrbtText": "shows ringback tone text from the caller",
    "CscFeature_Setting_ConfigAboutDeviceItems": "changes what About device shows",
    "CscFeature_SystemUI_SupportAssistanceAppChooser": "lets the assistant app be chosen",
    "CscFeature_Contact_ConfigImsOpStyle": "sets the Contacts icon style",
    "CscFeature_Contact_ConfigOpStyleVariation": "sets the Contacts icon style variant",
    "CscFeature_SystemUI_ConfigOpBrandingForIndicatorIcon": "sets the status bar indicator branding",
    "CscFeature_SystemUI_ConfigQuickSettingPopup": "sets the quick settings panel style",
    "CscFeature_DeviceSearch_AlwaysShowSipWhenSwipeLaunched": "shows the keyboard when the device search opens",
    "CscFeature_Common_SupportGmsAlarmManager": "turns the GMS alarm manager off, which can delay push",
    "CscFeature_Common_EnableVIPMode": "enables VIP mode",
    "CscFeature_SystemUI_SupportDataUsageViewOnQuickPanel": "shows data usage on the quick panel",
    "CscFeature_SystemUI_ConfigDefQuickSettingItem": "sets which tiles the quick panel starts with",
    "CscFeature_Common_ConfigDynamicLockScreenPolicy": "sets the dynamic lock screen style",
    "CscFeature_Common_SupportZProjectFunctionInGlobal": "enables the Z Project functions everywhere",
    "CscFeature_VoiceCall_ConfigOpStyleForBixbyTextCall": "enables Bixby text call",
    "CscFeature_VoiceCall_ConfigOpStyleForLiveTranslate": "enables live translation during calls",
}
for key, note in MZDYL.items():
    add(key, "mzdyl", description=note)

MZDYL_FF = {
    "SEC_FLOATING_FEATURE_SMARTMANAGER_CONFIG_PACKAGE_NAME": "changes which Smart Manager package is used",
    "SEC_FLOATING_FEATURE_SECURITY_CONFIG_DEVICEMONITOR_PACKAGE_NAME": "changes which device monitor package is used",
    "SEC_FLOATING_FEATURE_SETTINGS_SUPPORT_AUTO_POWER_ON_OFF": "adds auto power on and off to Settings",
    "SEC_FLOATING_FEATURE_AUDIO_SUPPORT_MICMODE_QUICK_PANEL": "adds the microphone mode quick panel switch",
    "SEC_FLOATING_FEATURE_AUDIO_SUPPORT_VOIP_VIA_SMART_MONITOR": "routes VoIP calls through the smart monitor",
    "SEC_FLOATING_FEATURE_BATTERY_SUPPORT_BSOH_GALAXYDIAGNOSTICS": "adds battery health to Galaxy Diagnostics",
    "SEC_FLOATING_FEATURE_BATTERY_SUPPORT_BSOH_SETTINGS": "adds battery health to Settings",
    "SEC_FLOATING_FEATURE_BATTERY_SUPPORT_PASS_THROUGH": "enables pass through charging",
    "SEC_FLOATING_FEATURE_BIXBY_SUPPORT_BIXBYKWD": "enables Bixby wake word detection",
    "SEC_FLOATING_FEATURE_BIXBY_SUPPORT_SANXINGXIAOBEIKWD": "enables the Chinese Bixby wake word",
    "SEC_FLOATING_FEATURE_COMMON_SUPPORT_BIXBY_TOUCH": "enables Bixby Touch",
    "SEC_FLOATING_FEATURE_COMMON_SUPPORT_CARLIFE": "enables Baidu CarLife",
    "SEC_FLOATING_FEATURE_COMMON_GOOGLE_AI_SEARCH": "enables Google AI search",
    "SEC_FLOATING_FEATURE_FRAMEWORK_SUPPORT_SMART_SUGGESTIONS_WIDGET": "enables the smart suggestions widget",
    "SEC_FLOATING_FEATURE_GENAI_SUPPORT_OFFLINE_LANGUAGEMODEL": "enables the on-device language model",
    "SEC_FLOATING_FEATURE_LCD_SUPPORT_EXTRA_BRIGHTNESS": "enables extra brightness, which is what outdoor mode uses",
    "SEC_FLOATING_FEATURE_SYSTEM_SUPPORT_ENHANCED_CPU_RESPONSIVENESS": "enables enhanced CPU responsiveness",
    "SEC_FLOATING_FEATURE_SYSTEM_SUPPORT_ENHANCED_PROCESSING": "enables enhanced processing",
    "SEC_FLOATING_FEATURE_SYSTEM_SUPPORT_LOW_HEAT_MODE": "enables low heat mode",
    "SEC_FLOATING_FEATURE_COMMON_SUPPORT_SAMSUNG_MARKETING_INFO": "turns Samsung marketing information off",
    "SEC_FLOATING_FEATURE_GRAPHICS_SUPPORT_TOUCH_FAST_RESPONSE": "enables the high touch sampling rate",
    "SEC_FLOATING_FEATURE_FRAMEWORK_SUPPORT_PERSONALIZED_DATA_CORE": "enables the personalized data core",
    "SEC_FLOATING_FEATURE_WLAN_SUPPORT_SECURE_WIFI": "turns Secure Wi-Fi off",
    "SEC_FLOATING_FEATURE_WIFI_SUPPORT_ADPS": "enables Wi-Fi power saving",
    "SEC_FLOATING_FEATURE_LCD_CONFIG_AOD_FULLSCREEN": "sets how much of the screen always on display uses",
    "SEC_FLOATING_FEATURE_COMMON_CONFIG_DEX_MODE": "picks which DeX modes exist",
    "SEC_FLOATING_FEATURE_AUDIO_SUPPORT_BT_RECORDING": "enables recording over Bluetooth",
    "SEC_FLOATING_FEATURE_AUDIO_SUPPORT_RECORDING_POPUP": "shows the recording popup",
    "SEC_FLOATING_FEATURE_AUDIO_SUPPORT_VOICE_CHANGER": "enables the voice changer",
    "SEC_FLOATING_FEATURE_BATTERY_SUPPORT_WIRELESS_TX": "enables wireless power sharing",
    "SEC_FLOATING_FEATURE_BIXBY_SUPPORT_LONG_KEY_SERVICE": "enables the long press Bixby service",
    "SEC_FLOATING_FEATURE_CAMERA_SUPPORT_DOWNLOAD_EFFECT": "allows camera effects to be downloaded",
    "SEC_FLOATING_FEATURE_CAMERA_SUPPORT_DUAL_PORTRAITVIDEO": "enables dual portrait video",
    "SEC_FLOATING_FEATURE_CAMERA_SUPPORT_PRO_RGB_CONVERSION": "enables RGB conversion in pro mode",
    "SEC_FLOATING_FEATURE_CAMERA_SUPPORT_QRCODE": "enables camera QR code scanning",
    "SEC_FLOATING_FEATURE_SYSTEMUI_SUPPORT_BRIEF_NOTIFICATION": "enables the brief notification style",
    "SEC_FLOATING_FEATURE_SYSTEM_SUPPORT_SCREEN_CURTAIN": "enables screen curtain",
    "SEC_FLOATING_FEATURE_VISION_SUPPORT_AI_MY_FAVORITE_CONTENTS": "enables AI favourite content",
}
for key, note in MZDYL_FF.items():
    add(key, "mzdyl", description=note)

# --- 4. the lists in el0xren/Samsung_Additional_Features, whose headings name the features
# The fork of those lists was updated after the original, and carries keys the original does not.
LISTS = [(REFS / "el0xren" / "floatingfeature.md", "el0xren"),
         (REFS / "el0xren" / "cscfeature.md", "el0xren"),
         (REFS / "ravindu-floatingfeature.md", "ravindu"),
         (REFS / "ravindu-cscfeature.md", "ravindu")]
for f, source in LISTS:
    if not f.exists():
        continue
    heading = None
    for line in f.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("###"):
            heading = line.lstrip("# ").strip()
        # Only a heading that reads like a description is used as one. Those lists also carry plain
        # section names such as "SystemUI" or "Smart Manager", which say nothing about a single key.
        descriptive = None
        # These lists number their entries, and a few name the feature and the value it needs.
        cleaned = re.sub(r"^\d+\.\s*", "", re.sub(r"\s*\(.*?\)\s*$", "", heading or "")).strip()
        if cleaned and (len(cleaned.split()) >= 3 or
                        any(v in cleaned.lower() for v in ("enable", "disable", "support"))):
            # Only a heading that opens with a verb is lowered; ones opening with an acronym such as
            # NFC or USIM would otherwise be mangled to nFC and uSIM.
            verb = ("Enable", "Disable", "Add", "Show", "Hide", "Remove", "Support", "Allow",
                    "Change", "Use", "Set", "Force", "Make", "Stop", "Keep")
            descriptive = (cleaned[0].lower() + cleaned[1:]) if cleaned.split()[0] in verb else cleaned
        for key, value in re.findall(
                r"<((?:CscFeature_|SEC_FLOATING_FEATURE_)[A-Za-z0-9_]+)>([^<]*)", line):
            add(key, source, description=descriptive, value=value)

# --- 5. the values this device's own files hold, and the carrier files behind them
device = json.loads((TMP / "devicecfg" / "device-gates.json").read_text(encoding="utf-8"))
for table, block in (("csc", device["csc"]), ("floating", device["floating"])):
    for key, value in block.items():
        add(key, "device", value=value)

# --- choose a category for everything, and a description where one is missing
for e in entries.values():
    # The area comes from the key itself, which is steadier than the app that reads it: a broad app
    # such as the camera reads keys belonging to other areas as well. Who reads it stays in the data.
    e["category"] = area_of(e["key"]) or "Other"
    if e["key"] in VERIFIED:
        e["verified"] = VERIFIED[e["key"]]
    if not e["description"]:
        e["description"] = derived(e["key"])
        e["description_source"] = "the key name"
    # One value is shown per key: the value the references agree on, which is what the feature is
    # switched on with, or failing that the value this device holds. Where the references disagree,
    # which they do for carrier specific keys, every value is in the data and none is picked out.
    given = {s: v for s, v in e["values"].items() if s != "device"}
    if len(set(given.values())) == 1 and given:
        e["value"] = next(iter(given.values()))
    elif "device" in e["values"]:
        e["value"] = e["values"]["device"]

json.dump({k: v for k, v in sorted(entries.items()) if v["table"] == "csc"},
          open(OUT / "data" / "csc.json", "w", encoding="utf-8"), indent=1)
json.dump({k: v for k, v in sorted(entries.items()) if v["table"] == "floating"},
          open(OUT / "data" / "floating.json", "w", encoding="utf-8"), indent=1)

csc = [e for e in entries.values() if e["table"] == "csc"]
floating = [e for e in entries.values() if e["table"] == "floating"]


def write_list(path, items, title, table_note):
    by_cat = defaultdict(list)
    for e in items:
        by_cat[e["category"]].append(e)
    lines = [f"# {title}", "", table_note, "",
             f"{len(items)} keys, grouped by the area they belong to. Each carries the value the "
             f"references give for it where they agree on one, or the value this device holds where "
             f"they do not. Where no reference describes a key, its note is a paraphrase of the key "
             f"name; the `description_source` field in the data says where a note came from.", ""]
    for cat in sorted(by_cat, key=lambda c: (-len(by_cat[c]), c)):
        lines += [f"## {cat}", ""]
        for e in sorted(by_cat[cat], key=lambda e: e["key"]):
            value = f" = `{e['value']}`" if e.get("value") else ""
            lines.append(f"- `{e['key']}`{value} - {e['description']}")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


write_list(
    OUT / "csc-features.md", csc, "Samsung CSC features",
    "The CSC table, which carriers fill in and the framework reads, and which has to be answered "
    "rather than written on a device that does not let an app change it.",
)
write_list(
    OUT / "floating-features.md", floating, "Samsung floating features",
    "The floating feature table, which the build fills in and the framework reads.",
)

described = sum(1 for e in entries.values() if e["description_source"] != "the key name")
print(f"total {len(entries)} keys: {len(csc)} csc, {len(floating)} floating")
print(f"with a description from a reference: {described}, derived from the name: {len(entries) - described}")
print(f"seen in the ROM scan: {sum(1 for e in entries.values() if 'scan' in e['from'])}")
print(f"in the KOO carrier file: {sum(1 for e in entries.values() if 'koo' in e['from'])}")
print(f"with a value from this device: {sum(1 for e in entries.values() if 'device' in e['values'])}")
print(f"showing a value: {sum(1 for e in entries.values() if e['value'])}")
print(f"with more than one value recorded: {sum(1 for e in entries.values() if len(e['values']) > 1)}")
print(f"checked on a device: {sum(1 for e in entries.values() if e.get('verified'))}")
print("categories:", len({e['category'] for e in entries.values()}))
for f in sorted(OUT.rglob("*")):
    if f.is_file():
        print(f"  {f.relative_to(OUT)}  {f.stat().st_size}")
