# Samsung CSC and floating features

The feature switches Samsung keeps on a device: what each key is called, what it switches and the
value it takes, gathered from the community projects that document them and from a real One UI 8
phone.

Samsung decides what a phone can do from two tables that are fixed at build time:

- **CSC features** (`CscFeature_*`), which the carrier configuration fills in. A carrier that does not
  set a key leaves the feature at the framework's default.
- **Floating features** (`SEC_FLOATING_FEATURE_*`), which the firmware fills in, keyed by the model.

Neither table can be changed by an app on a stock device - the CSC files are obfuscated and the build
files are read only - so tools that unlock these features answer the lookup at run time instead. That
is what the lists here are for: knowing which key to answer, and what answering it does.

## What is here

| File | What it holds |
|------|----------------|
| [csc-features.md](csc-features.md) | 580 CSC keys, grouped by area, each with a value and a note |
| [floating-features.md](floating-features.md) | 507 floating feature keys, grouped by area, likewise |
| `data/csc.json`, `data/floating.json` | the same entries as data: area, note, where the note came from, the value shown, **every value each source gives**, which apps read the key, and which sources list it at all |
| [tools/](tools) | the scripts used to build the lists, so they can be rebuilt or extended |

A key that several projects list appears once, with all of its sources recorded rather than repeated,
and a key whose sources disagree about its value keeps every value in the data instead of having one
picked for it.

Every entry carries where it came from, so nothing is asserted without a source:

| Source | What it is | Entries it added | Descriptions it provided |
|--------|-----------|------------------|--------------------------|
| `scan` | the keys read by the system apps of a One UI 8 device (SM-S938U1), found by searching each app's code and native libraries | 516 | 0 |
| `device` | the carrier and floating feature files of that device, which contribute their own values | 401 | 0 |
| `koo` | the complete carrier CSC file shipped in [y6yuan/SamsungKOO2CHC](https://github.com/y6yuan/SamsungKOO2CHC) | 229 | 0 |
| `mzdyl` | the config tables in [Mzdyl/OneUI_CSC_Features](https://github.com/Mzdyl/OneUI_CSC_Features) | 85 | 85 |
| `el0xren` | the CSC and floating feature lists in [el0xren/Samsung_Additional_Features](https://github.com/el0xren/Samsung_Additional_Features) | 337 | 43 |
| `ravindu` | the same two lists in [ravindu644/Samsung_Additional_Features](https://github.com/ravindu644/Samsung_Additional_Features), a fork updated after the original, which adds keys the original does not carry | 349 | 41 |

**About the descriptions.** 169 keys carry a description taken from one of the reference lists - 85
from the Mzdyl tables, 43 from the el0xren lists, 41 from the fork. The other 918 were not described
anywhere I could find, so their note is read out of the key itself and marked ***(from the key
name)*** in the lists. Those are a paraphrase of a name, not documentation of behaviour - treat them
as a starting point, not a promise. The `description_source` field in the JSON says where each note
came from.

## How the list was built

1. **Every key the system reads**, found by searching the code and native libraries of the device's
   own system apps (`tools/scan-apk.py`). This is the part that makes the list match a real ROM
   rather than a wish list: a key that no app on this device asks for is a key that does nothing here.
   It also records *which* app reads each key, which is kept in the JSON.
2. **Every key in the community lists**, taken from the repositories named above.
3. **The device's own carrier files**, decoded first. That obfuscation is not encryption: every byte
   is rotated left by a value from one fixed table, XORed with a value from another, and the result is
   gzipped (`tools/decode-omc.py`). The two tables come from the decoder in the OneUI_CSC_Features
   repository, and [fei-ke/OmcTextDecoder](https://github.com/fei-ke/OmcTextDecoder) is the original
   tool for the same job.
4. **Merged, deduplicated, and grouped** by the area in the key itself (`tools/build-lists.py`). The
   area comes from the key rather than from the app that reads it, because a busy app such as the
   camera reads keys belonging to other areas too.

## Tested on a device

Most keys here have never been tried; they are what the sources say, not what has been seen working.
Where a key has been tried on a real phone, the result is kept in the `verified` field of its entry,
and the two so far are worth writing down because both look like failures at first glance:

| Key | What was seen |
|-----|----------------|
| `SEC_FLOATING_FEATURE_BATTERY_SUPPORT_BSOH_SETTINGS` | With the gate on and then off, About phone > Battery information shows battery health, cycle count and capacity either way. Those rows come from somewhere else - on that phone, a module feature that unhides the page - so this key did not control them. |
| `CscFeature_Setting_EnableHwVersionDisplay` | No hardware version row appears in About phone. Worth noting the value was entered as `true` where the references give `TRUE`, so the case may be what matters. |

## Using it

- **With a run-time module** such as [One UI X](https://github.com/SoClear/OneUIX): the gate list in
  that module reads the device's own files and lets any key be answered with another value. These
  lists tell you which key to look for.
- **With file based modules** such as OneUI_CSC_Features or SamsungKOO2CHC: their config files take
  `key` and `value` pairs, which is the same shape as the JSON here.
- **On a device**, to see what a key currently answers, decode the carrier file with
  `tools/decode-omc.py`, or search for the key in `/system/etc/floating_feature.xml` and
  `/vendor/etc/floating_feature.xml`, which are plain XML.

## Things worth knowing

- **A value is not portable.** The values shown come from the projects' own config files, and where
  those disagree, from a single device with one carrier. Another carrier or model can hold a different
  value for the same key, and some keys are only read by the firmware of a particular model. Treat a
  value as a starting point and check what your own device holds.
- **Answering a key is not the same as changing a feature.** A feature implemented in native code
  that parses the floating feature file itself, without going through the framework's table, will not
  see an answer given at the framework level.
- **Some keys are build-time only.** `SEC_FLOATING_FEATURE_*` values are read while an app starts, so
  a feature that was already read before a change takes effect keeps its old value until that app is
  restarted.
- **Nothing here is Samsung documentation.** Keys were collected from firmware and from the community
  projects credited below; the descriptions that came from them are reproduced in short form.

## Credits

The community projects this list is built on, and what each contributed:

- [Mzdyl/OneUI_CSC_Features](https://github.com/Mzdyl/OneUI_CSC_Features) - the CSC and floating
  feature config tables, and the decoder whose two tables make the carrier files readable.
- [el0xren/Samsung_Additional_Features](https://github.com/el0xren/Samsung_Additional_Features) - the
  floating feature, CSC feature and build.prop tweak lists.
- [ravindu644/Samsung_Additional_Features](https://github.com/ravindu644/Samsung_Additional_Features) -
  a fork of those lists carrying a later revision, which is where several keys and descriptions the
  original lacks came from.
- [y6yuan/SamsungKOO2CHC](https://github.com/y6yuan/SamsungKOO2CHC) - a complete carrier CSC file and
  its network features, which is where the largest single contribution of real keys came from.
- [fei-ke/OmcTextDecoder](https://github.com/fei-ke/OmcTextDecoder) - the original tool for decoding
  Samsung's OMC files.

Worth reading, and credited as related work in the same space:

- [NcX ROM features pack](https://xdaforums.com/t/ncx-rom-features-pack-magisk-module.4583543/) - a
  module of ROM style tweaks for Samsung devices.
- [Decoded_CSC_Features_Files_AIO](https://xdaforums.com/t/magisk-module-exynos-snapdragon-test-decoded_csc_features_files-esim-support.4082445/)
  - decoded carrier CSC files, with eSIM support.

Both are forum threads rather than repositories, and their pages turn away automated readers, so the
keys they list are not part of this compilation yet. Adding them would be a welcome contribution.

Key names and values belong to Samsung. This compilation belongs to whoever wants it.
