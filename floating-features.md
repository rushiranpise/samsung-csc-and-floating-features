# Samsung floating features

The floating feature table, which the build fills in and the framework reads.

507 keys, grouped by the area they belong to. Each carries the value the references give for it where they agree on one, or the value this device holds where they do not. Where no reference describes a key, its note is a paraphrase of the key name; the `description_source` field in the data says where a note came from.

## Camera

- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_ACTION_CLASSIFIER` = `1,0` - Camera: sets action classifier
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_AIFRC_EXTENSIONS` = `MP_PLAYBACK_SPEC:480,480,1920,1440,23,31,HDR` - Camera: sets aifrc extensions
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_AIFRC_SPEC` = `480,480,3840,2160,23,61,HDR` - Camera: sets aifrc spec
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_AI_DEFLICKER` = `OFF` - Camera: sets ai deflicker
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_AI_HIGH_RESOLUTION_MAX_CAPTURE` = `-1` - Camera: sets ai high resolution max capture
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_AUTOFRAMING` = `uhd` - Camera: sets autoframing
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_AVATAR_MAX_FACE_NUM` = `3` - Camera: sets avatar max face num
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_CAMID_BOKEH` = `-1` - Camera: sets camid bokeh
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_CAMID_MACRO` = `-1` - Camera: sets camid macro
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_CAMID_TELE2` = `54` - Camera: sets camid tele2
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_CAMID_TELE_BINNING` = `-1` - Camera: sets camid tele binning
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_CAMID_TELE_STANDARD_CROP` = `52` - Camera: sets camid tele standard crop
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_CAMID_UW` = `58` - Camera: sets camid uw
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_CAMID_WIDE` = `56` - Camera: sets camid wide
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_CORE_VERSION` = `v2` - Camera: sets core version
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_GALAXYRAW_PLATFORM_VERSION` = `17.06.01` - Camera: sets galaxyraw platform version
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_GPPM_SOLUTIONS` = `startrail,motionclipper` - Camera: sets gppm solutions
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_HIGH_RESOLUTION_MAX_CAPTURE` = `0` - Camera: sets high resolution max capture
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_IS_GPPM_1_0_ENABLED` = `TRUE` - Camera: sets is gppm 1 0 enabled
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_LLHDR_PROCESSING_TIMEOUT` = `2000` - Camera: sets llhdr processing timeout
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_LOG_VIDEO` = `V1.0` - Camera: sets log video
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_MEMORY_USAGE_LEVEL` = `2` - Camera: sets memory usage level
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_MOIRE_REMOVAL` = `OFF` - Camera: sets moire removal
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_MOTIONPHOTO_CAPTURE_MODE` = `[[3,1],[3,0.5]]` - Camera: sets motionphoto capture mode
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_MOTIONPHOTO_DEFAULT_SOUND_TIMING` = `picture_taken` - Camera: sets motionphoto default sound timing
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_MOTIONPHOTO_DEFAULT_SOUND_TYPE` = `camera_shutter` - Camera: sets motionphoto default sound type
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_MYFILTER` = `1,3,4` - Camera: sets myfilter
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_NIGHT_FRONT_BEAUTY_LEVEL` = `2` - Camera: sets night front beauty level
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_NIGHT_FRONT_DISPLAY_FLASH_TRANSPARENT` = `65` - Camera: sets night front display flash transparent
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_PERSONALIZATION` = `V3_SELFIE` - Camera: sets personalization
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_QRCODE_INTERVAL` = `250` - Camera: sets qrcode interval
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_SDK_FEATURE_INFO` = `version2,super_night,preview_dis,video_hdr,smooth_zoom,logical_rear_camera:camera_id=20,exposure_table_control,selfie_tone,physical_camera_tele:camera_id=52,physical_camera_tele2:camera_id=54,super_night_exposure` - Camera: sets sdk feature info
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_SINGLE_PORTRAIT_DISTORTION_CORRECTION` = `YUV` - Camera: sets single portrait distortion correction
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_STRIDE_OCR_VERSION` = `V2` - Camera: sets stride ocr version
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_SUPERSTEADY_POPUP` = `256` - Camera: sets supersteady popup
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_UW_DISTORTION_CORRECTION` = `0,109,2,24100702,4000,3000,3,0,60,0` - Camera: sets uw distortion correction
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_VENDOR_LIB_INFO` = `de_flicker.arcsoft.v1,ai_isp.samsung.v1,food.samsung.v1,beauty.samsung.v4,facial_restoration.arcsoft.v1,face_landmark.arcsoft.v2_1,facial_attribute.samsung.v1,human_tracking_hand.arcsoft.v4,fr_tracking.arcsoft.v1,ai_clear_zoom.arcsoft.v2,hybridhdr.arcsoft.v1,aebhdr.arcsoft.v1,super_night.mpi.v2,aimode.samsung.v3,super_resolution_tetra.samsung.v1,image_codec.samsung.v2,single_bokeh.samsung.v2,dual_bokeh.samsung.v2,image_enhance.arcsoft.v1,stereo_photo.samsung.v1,smart_scan.samsung.v2,swuwdc.arcsoft.v1,selfie_correction.samsung.v2,event_detection.samsung.v2,pro_single_rgb.mpi.v1,localtm.samsung.v1_1,mid_highres.samsung.v1` - Camera: sets vendor lib info
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_VERSION_FILTER_PROVIDER` = `8` - Camera: sets version filter provider
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_WIDE_DISTORTION_CORRECTION` = `0,109,2,23111001,4000,3000,0,150,60,0` - Camera: sets wide distortion correction
- `SEC_FLOATING_FEATURE_CAMERA_CONFIG_WINE_DETECTOR` = `V1_SNAP_CPU` - Camera: sets wine detector
- `SEC_FLOATING_FEATURE_CAMERA_DOCUMENTSCAN_SOLUTIONS` = `AI_DEWARPING,SHADOW_REMOVAL,DEBLUR,OBJECT_REMOVAL,COLOR_ENHANCE,TEXT_REFLECTION_REMOVAL,MOIRE_REMOVAL,DOGEAR_REMOVAL,SCANNER_FILTER,DEFAULT_COLOR_FILTER,MAGNET` - Camera: documentscan solutions
- `SEC_FLOATING_FEATURE_CAMERA_GRAW_CONFIG_MFP_PIPELINE_MODE` = `V6` - Camera: graw config mfp pipeline mode
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_30FPS_ALL_PORTRAITVIDEO` = `TRUE` - Camera: adds 30 fps all portraitvideo
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_4K_PORTRAITVIDEO` = `TRUE` - Camera: adds 4 k portraitvideo
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_AFSENSITIVITY` - Camera: adds afsensitivity
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_AFSKIP` = `TRUE` - Camera: adds afskip
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_AFSPEED` - Camera: adds afspeed
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_AF_DURING_SLOWMOTION_RECORDING` - Camera: adds af during slowmotion recording
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_AIFRC` = `TRUE` - Camera: adds aifrc
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_AI_HIGH_RESOLUTION` = `TRUE` - Camera: adds ai high resolution
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_AI_HIGH_RESOLUTION_DRAFT_DOWNSCALE` = `TRUE` - Camera: adds ai high resolution draft downscale
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_AUTO_EXPOSURE_LIMIT` = `TRUE` - Camera: adds auto exposure limit
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_AVATAR` = `TRUE` - Camera: adds avatar
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_CAPTURE_SELFIE_CORRECTION` - Camera: adds capture selfie correction
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_CINEMATIC_PORTRAITVIDEO` - Camera: adds cinematic portraitvideo
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_CONTROLLING_WATCH` = `TRUE` - Camera: adds controlling watch
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_DOWNLOAD_EFFECT` = `TRUE` - allows camera effects to be downloaded
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_DUAL_PORTRAITVIDEO` = `TRUE` - enables dual portrait video
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_EDITABLE_PORTRAITVIDEO` = `TRUE` - Camera: adds editable portraitvideo
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_FUSION_HIGH_RESOLUTION` - Camera: adds fusion high resolution
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_GALLERY_LR` = `TRUE` - Camera: adds gallery lr
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_HIGH_RESOLUTION_MEMORY_CHECK` - Camera: adds high resolution memory check
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_HIGH_RESOLUTION_SWBINNING` = `TRUE` - Camera: adds high resolution swbinning
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_HYPERLAPSE_VDISONOFF` = `TRUE` - Camera: adds hyperlapse vdisonoff
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_LOGICAL_CAMERA` = `true` - Camera: adds logical camera
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_MACRO_RAW_SR_DRAFT_RAW` - Camera: adds macro raw sr draft raw
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_MOTIONPHOTO_AUTO_TRIM_MODE` = `TRUE` - Camera: adds motionphoto auto trim mode
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_MOTIONPHOTO_SOUND_TIMING` = `TRUE` - Camera: adds motionphoto sound timing
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_MOTIONPHOTO_SOUND_TYPE` = `TRUE` - Camera: adds motionphoto sound type
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_NIGHT_FRONT_DISPLAY_FLASH` = `true` - Camera: adds night front display flash
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_NIGHT_INTEGRATED_PHOTO_MODE` - Camera: adds night integrated photo mode
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_OISCENTERING_PORTRAITVIDEO` - Camera: adds oiscentering portraitvideo
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_PORTRAIT_INTELLIGENT_OPTIMIZATION_AI_ISP` = `TRUE` - Camera: adds portrait intelligent optimization ai isp
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_PREWARMING_LEVEL` = `0` - Camera: adds prewarming level
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_PRIVACY_TOGGLE` = `TRUE` - Camera: adds privacy toggle
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_PRO_RGB_CONVERSION` = `TRUE` - enables RGB conversion in pro mode
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_QRCODE` = `TRUE` - enables camera QR code scanning
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_SEAMLESS_PORTRAITVIDEO` = `TRUE` - Camera: adds seamless portraitvideo
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_SUPER_NIGHT_DRAFT_RAW` = `TRUE` - Camera: adds super night draft raw
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_TORCH_BRIGHTNESS_LEVEL` = `TRUE` - Camera: adds torch brightness level
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_VDIS_ON_MOTIONPHOTO` = `TRUE` - Camera: adds vdis on motionphoto
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_VDIS_PORTRAITVIDEO` = `TRUE` - Camera: adds vdis portraitvideo
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_VIDEO_PALM` = `TRUE` - Camera: adds video palm
- `SEC_FLOATING_FEATURE_CAMERA_SUPPORT_VIDEO_SOFTENING` - Camera: adds video softening

## Common

- `SEC_FLOATING_FEATURE_COMMON_CONFIG_AI_VERSION` = `20263` - Common: sets ai version
- `SEC_FLOATING_FEATURE_COMMON_CONFIG_AWESOME_INTELLIGENCE` - Common: sets awesome intelligence
- `SEC_FLOATING_FEATURE_COMMON_CONFIG_B2BCODE` - Common: sets b2 bcode
- `SEC_FLOATING_FEATURE_COMMON_CONFIG_CMH_SIOP_LEVEL` = `2` - Common: sets cmh siop level
- `SEC_FLOATING_FEATURE_COMMON_CONFIG_DAILYBOARD` - Common: sets dailyboard
- `SEC_FLOATING_FEATURE_COMMON_CONFIG_DEVICE_MANUFACTURING_TYPE` = `in_house` - Common: sets device manufacturing type
- `SEC_FLOATING_FEATURE_COMMON_CONFIG_DEX_MODE` - picks which DeX modes exist
- `SEC_FLOATING_FEATURE_COMMON_CONFIG_DYN_RESOLUTION_CONTROL` = `WQHD,FHD,HD` - enable 3 Resolution options in Settings
- `SEC_FLOATING_FEATURE_COMMON_CONFIG_EDGE` = `people,task,circle,panel,-edgefeeds,edgelighting_v2,debug,cornerR:6.2,search,phonecolor,dot_bottom` - enable Flagship Edge Ligthining+ Animations in Q
- `SEC_FLOATING_FEATURE_COMMON_CONFIG_EMBEDDED_SIM_SLOTSWITCH` - Common: sets embedded sim slotswitch
- `SEC_FLOATING_FEATURE_COMMON_CONFIG_GESTUREWAKEUP_CHANGEMIC` = `0` - Common: sets gesturewakeup changemic
- `SEC_FLOATING_FEATURE_COMMON_CONFIG_GESTUREWAKEUP_EXTRTO` = `0,0` - Common: sets gesturewakeup extrto
- `SEC_FLOATING_FEATURE_COMMON_CONFIG_GESTUREWAKEUP_NORMRTO` = `0,0` - Common: sets gesturewakeup normrto
- `SEC_FLOATING_FEATURE_COMMON_CONFIG_GESTUREWAKEUP_VERSION` = `0` - Common: sets gesturewakeup version
- `SEC_FLOATING_FEATURE_COMMON_CONFIG_HOMEHUB` - Common: sets homehub
- `SEC_FLOATING_FEATURE_COMMON_CONFIG_MDNIE_MODE` = `65303` - Common: sets mdnie mode
- `SEC_FLOATING_FEATURE_COMMON_CONFIG_MULTIMEDIA_EDITOR_PLUGIN_PACKAGES` = `videoeditor,videotrimmer,videocollage,projectpicker,multiedit` - Common: sets multimedia editor plugin packages
- `SEC_FLOATING_FEATURE_COMMON_CONFIG_MULTIWINDOW_TRAY` = `TRUE` - enable Multiwindow tray
- `SEC_FLOATING_FEATURE_COMMON_CONFIG_OMC_VERSION` = `5.1` - Common: sets omc version
- `SEC_FLOATING_FEATURE_COMMON_CONFIG_ONEHAND_MODE_POLICY` = `Enabled;GestureType` - Common: sets onehand mode policy
- `SEC_FLOATING_FEATURE_COMMON_CONFIG_SEP_CATEGORY` = `sep_basic` - Common: sets sep category
- `SEC_FLOATING_FEATURE_COMMON_CONFIG_SMARTTUTOR_PACKAGES_NAME` = `com.rsupport.rs.activity.rsupport.aas2` - Common: sets smarttutor packages name
- `SEC_FLOATING_FEATURE_COMMON_CONFIG_SMARTTUTOR_PACKAGES_PATH` = `system/hidden/SmartTutor/SmartTutor.apk` - Common: sets smarttutor packages path
- `SEC_FLOATING_FEATURE_COMMON_CONFIG_SPEN_SENSITIVITY_ADJUSTMENT` = `900` - Common: sets spen sensitivity adjustment
- `SEC_FLOATING_FEATURE_COMMON_CONFIG_SWLENS_DISTORTION_CORRECTION` - Common: sets swlens distortion correction
- `SEC_FLOATING_FEATURE_COMMON_CONFIG_VDC` - Common: sets vdc
- `SEC_FLOATING_FEATURE_COMMON_CONFIG_WAKEUP_MULTIAGENT_VERSION` = `0` - Common: sets wakeup multiagent version
- `SEC_FLOATING_FEATURE_COMMON_DISABLE_NATIVE_AI` - Common: turns off native ai
- `SEC_FLOATING_FEATURE_COMMON_DISABLE_RECYCLE_BIN` - Common: turns off recycle bin
- `SEC_FLOATING_FEATURE_COMMON_GOOGLE_AI_SEARCH` = `TRUE` - enables Google AI search
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_AI_AGENT` = `TRUE` - Common: adds ai agent
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_BATTERY_CONVERSING` - Common: adds battery conversing
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_BIXBY` = `TRUE` - Common: adds bixby
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_BIXBY_TOUCH` = `TRUE` - enables Bixby Touch
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_BLE_SPEN` - Common: adds ble spen
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_CARLIFE` = `TRUE` - enables Baidu CarLife
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_COLOR_LENS` = `TRUE` - Common: adds color lens
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_DESKTOP_WINDOWING` = `TRUE` - Common: adds desktop windowing
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_DEX_MULTI_RATIO` = `TRUE` - enable Wireless PowerShare
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_DEX_ON_PC` = `TRUE` - enable Wireless PowerShare
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_DEX_WIRELESS` = `TRUE` - enable Wireless PowerShare
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_DISABLED_MENU_K05` - Common: adds disabled menu k05
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_DISABLED_MENU_N40` - Common: adds disabled menu n40
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_DISABLE_DATA_SERVICE` - Common: adds disable data service
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_DISPLAY_CUTOUT` - Common: adds display cutout
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_ELASTIC_PLUGIN` = `TRUE` - Common: adds elastic plugin
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_EMBEDDED_SIM` - Common: adds embedded sim
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_EVS` = `TRUE` - Common: adds evs
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_FLASH_NOTIFICATION` = `TRUE` - Common: adds flash notification
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_HDR_EFFECT` = `TRUE` - Common: adds hdr effect
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_HEADLESS_DEVICE` - Common: adds headless device
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_HIGH_PERFORMANCE_MODE` = `TRUE` - enable High Performance Mode
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_KNOX_DESKTOP` - Common: adds knox desktop
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_LTW_REMOTE_APP` = `TRUE` - Common: adds ltw remote app
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_NAL_PRELOADAPP_REGULATION` - Common: adds nal preloadapp regulation
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_NFC_HW_KEYBOARD` - Common: adds nfc hw keyboard
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_PTT` - Common: adds ptt
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_SAFETYCARE` - Common: adds safetycare
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_SAMSUNG_MARKETING_INFO` = `FALSE` - turns Samsung marketing information off
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_SECUREUI_LANDSCAPE` = `TRUE` - Common: adds secureui landscape
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_SMART_SWITCH` = `FALSE` - disable Smart Switch
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_ULTRA_POWER_SAVING` = `TRUE` - enable Ultra Power Saving
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_UNPACK` - Common: adds unpack
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_VARIABLE_REFRESH_RATE` - Common: adds variable refresh rate
- `SEC_FLOATING_FEATURE_COMMON_SUPPORT_WEARABLE_GLASSES` = `TRUE` - Common: adds wearable glasses

## Audio

- `SEC_FLOATING_FEATURE_AUDIO_CONFIG_ADAPTSOUND_VERSION` - Audio: sets adaptsound version
- `SEC_FLOATING_FEATURE_AUDIO_CONFIG_ASSISTANT_SPEAKER_MAX_VOLUME` = `12` - Audio: sets assistant speaker max volume
- `SEC_FLOATING_FEATURE_AUDIO_CONFIG_EFFECTS_VIDEOCALL` = `None` - Audio: sets effects videocall
- `SEC_FLOATING_FEATURE_AUDIO_CONFIG_INTERPRETER` = `1` - Audio: sets interpreter
- `SEC_FLOATING_FEATURE_AUDIO_CONFIG_JDM_ITEMS` - Audio: sets jdm items
- `SEC_FLOATING_FEATURE_AUDIO_CONFIG_MIC_POSITION` = `screen_rec_1_mic` - Audio: sets mic position
- `SEC_FLOATING_FEATURE_AUDIO_CONFIG_MULTIRECORD` = `10` - Audio: sets multirecord
- `SEC_FLOATING_FEATURE_AUDIO_CONFIG_MULTISOURCE_SEPARATOR` = `{FastScanning_6, SourceSeparator_4, Version_1.3.0}` - Audio: sets multisource separator
- `SEC_FLOATING_FEATURE_AUDIO_CONFIG_MULTI_MIC` = `3` - Audio: sets multi mic
- `SEC_FLOATING_FEATURE_AUDIO_CONFIG_REMOTE_MIC` = `DSP` - Audio: sets remote mic
- `SEC_FLOATING_FEATURE_AUDIO_CONFIG_SOUNDALIVE_VERSION` = `eq_custom,uhq_onoff,karaoke,adapt,spk_stereo,dvfs_20_percent,dvfs_max_45_percent,voice_boost` - enable Dolby Atmos without Headsets
- `SEC_FLOATING_FEATURE_AUDIO_CONFIG_VOLUMEMONITOR_GAIN` = `0` - Audio: sets volumemonitor gain
- `SEC_FLOATING_FEATURE_AUDIO_CONFIG_VOLUMEMONITOR_STAGE` = `2` - Audio: sets volumemonitor stage
- `SEC_FLOATING_FEATURE_AUDIO_NUMBER_OF_SPEAKER` = `1` - Audio: number of speaker
- `SEC_FLOATING_FEATURE_AUDIO_SUPPORT_ADAPT_SOUND_CALL_PARAM` = `TRUE` - Audio: adds adapt sound call param
- `SEC_FLOATING_FEATURE_AUDIO_SUPPORT_ANTI_HOWLING` - Audio: adds anti howling
- `SEC_FLOATING_FEATURE_AUDIO_SUPPORT_BIXBY_VOLUME_SEPARATION` - Audio: adds bixby volume separation
- `SEC_FLOATING_FEATURE_AUDIO_SUPPORT_BT_RECORDING` = `TRUE` - enables recording over Bluetooth
- `SEC_FLOATING_FEATURE_AUDIO_SUPPORT_CPU_LOCK_FOR_VOIP` - Audio: adds cpu lock for voip
- `SEC_FLOATING_FEATURE_AUDIO_SUPPORT_DC_MOTOR_HAPTIC_FEEDBACK` = `TRUE` - enable Haptic Feedback in settings
- `SEC_FLOATING_FEATURE_AUDIO_SUPPORT_DEFAULT_ON_DOLBY_IN_GAME` = `TRUE` - enable Dolby Atmos in Games
- `SEC_FLOATING_FEATURE_AUDIO_SUPPORT_DOLBY_GAME_PROFILE` = `TRUE` - enable Dolby Atmos Game Profiles
- `SEC_FLOATING_FEATURE_AUDIO_SUPPORT_DUAL_SPEAKER` = `TRUE` - enable Dolby Atmos without Headsets
- `SEC_FLOATING_FEATURE_AUDIO_SUPPORT_HEADTRACKING_EFFECT` = `TRUE` - Audio: adds headtracking effect
- `SEC_FLOATING_FEATURE_AUDIO_SUPPORT_MICMODE_QUICK_PANEL` = `TRUE` - adds the microphone mode quick panel switch
- `SEC_FLOATING_FEATURE_AUDIO_SUPPORT_MULTI_DEVICE_SOUND` - Audio: adds multi device sound
- `SEC_FLOATING_FEATURE_AUDIO_SUPPORT_RECORDING_POPUP` = `TRUE` - shows the recording popup
- `SEC_FLOATING_FEATURE_AUDIO_SUPPORT_SITUATION_EXTENSION` = `TRUE` - Audio: adds situation extension
- `SEC_FLOATING_FEATURE_AUDIO_SUPPORT_SPEAKER_AEC` - Audio: adds speaker aec
- `SEC_FLOATING_FEATURE_AUDIO_SUPPORT_TRANSITION_EFFECT` = `TRUE` - Audio: adds transition effect
- `SEC_FLOATING_FEATURE_AUDIO_SUPPORT_VOICE_CHANGER` = `TRUE` - enables the voice changer
- `SEC_FLOATING_FEATURE_AUDIO_SUPPORT_VOICE_TX_FOR_INCALL_MUSIC` = `TRUE` - Audio: adds voice tx for incall music
- `SEC_FLOATING_FEATURE_AUDIO_SUPPORT_VOIP_SOUND_LOUDER` - Audio: adds voip sound louder
- `SEC_FLOATING_FEATURE_AUDIO_SUPPORT_VOIP_VIA_SMART_MONITOR` = `TRUE` - routes VoIP calls through the smart monitor
- `SEC_FLOATING_FEATURE_AUDIO_SUPPORT_VOIP_VIA_SMART_VIEW` = `TRUE` - Audio: adds voip via smart view
- `SEC_FLOATING_FEATURE_AUDIO_SUPPORT_VOLUME_MONITOR` = `DSP` - Audio: adds volume monitor

## Framework

- `SEC_FLOATING_FEATURE_FRAMEWORK_CONFIG_AGENT_WITH_PDE` = `0` - Framework: sets agent with pde
- `SEC_FLOATING_FEATURE_FRAMEWORK_CONFIG_AOD_ITEM` = `aodversion=7,clocktransition,coverboldfont` - enable AOD Clock Transition Animation
- `SEC_FLOATING_FEATURE_FRAMEWORK_CONFIG_CLOCKPACK_ITEM` - Framework: sets clockpack item
- `SEC_FLOATING_FEATURE_FRAMEWORK_CONFIG_COVER` - Framework: sets cover
- `SEC_FLOATING_FEATURE_FRAMEWORK_CONFIG_FRAME_SPLIT_COUNT` = `13` - Framework: sets frame split count
- `SEC_FLOATING_FEATURE_FRAMEWORK_CONFIG_NAVIGATION_BAR_THEME` = `SupportLightNavigationBar|SupportCustomBgColor|SupportNaviBarRemoteView` - Framework: sets navigation bar theme
- `SEC_FLOATING_FEATURE_FRAMEWORK_CONFIG_NFC_LED_COVER_LEVEL` = `-1` - Framework: sets nfc led cover level
- `SEC_FLOATING_FEATURE_FRAMEWORK_CONFIG_NOW_NUDGE_VERSION` = `2` - Framework: sets now nudge version
- `SEC_FLOATING_FEATURE_FRAMEWORK_CONFIG_ROUNDED_CORNER_RADIUS` - Framework: sets rounded corner radius
- `SEC_FLOATING_FEATURE_FRAMEWORK_CONFIG_SCREEN_RECORDER_ITEM` = `-pip` - enable Advanced Screen Capture
- `SEC_FLOATING_FEATURE_FRAMEWORK_CONFIG_SPEN_GARAGE_SPEC` = `type=insert, bundled=true` - Framework: sets spen garage spec
- `SEC_FLOATING_FEATURE_FRAMEWORK_CONFIG_SPEN_VERSION` = `70` - Framework: sets spen version
- `SEC_FLOATING_FEATURE_FRAMEWORK_SUPPORT_AI_BRIEF_FOR_UT` - Framework: adds ai brief for ut
- `SEC_FLOATING_FEATURE_FRAMEWORK_SUPPORT_AOD_DOZE_SERVICE` - Framework: adds aod doze service
- `SEC_FLOATING_FEATURE_FRAMEWORK_SUPPORT_BLOCKCHAIN_SERVICE` = `TRUE` - Framework: adds blockchain service
- `SEC_FLOATING_FEATURE_FRAMEWORK_SUPPORT_CUSTOM_STARTING_WINDOW` = `TRUE` - Framework: adds custom starting window
- `SEC_FLOATING_FEATURE_FRAMEWORK_SUPPORT_EAGLE_EYE` - Framework: adds eagle eye
- `SEC_FLOATING_FEATURE_FRAMEWORK_SUPPORT_FOLDABLE_TYPE_FLIP` - Framework: adds foldable type flip
- `SEC_FLOATING_FEATURE_FRAMEWORK_SUPPORT_FOLDABLE_TYPE_FOLD` - Framework: adds foldable type fold
- `SEC_FLOATING_FEATURE_FRAMEWORK_SUPPORT_FOLDABLE_TYPE_LANDSCAPE_FOLD` - Framework: adds foldable type landscape fold
- `SEC_FLOATING_FEATURE_FRAMEWORK_SUPPORT_HALF_FOLDED_MODE` - Framework: adds half folded mode
- `SEC_FLOATING_FEATURE_FRAMEWORK_SUPPORT_LARGE_COVER_SCREEN` - Framework: adds large cover screen
- `SEC_FLOATING_FEATURE_FRAMEWORK_SUPPORT_MULTI_FOLD` - Framework: adds multi fold
- `SEC_FLOATING_FEATURE_FRAMEWORK_SUPPORT_PERSONALIZED_DATA_CORE` = `TRUE` - enables the personalized data core
- `SEC_FLOATING_FEATURE_FRAMEWORK_SUPPORT_PROVIDE_TSP_RAWDATA` = `TRUE` - Framework: adds provide tsp rawdata
- `SEC_FLOATING_FEATURE_FRAMEWORK_SUPPORT_SCREEN_CAPTURE_ADVANCED_EDIT_VI` = `TRUE` - enable Advanced Screen Capture
- `SEC_FLOATING_FEATURE_FRAMEWORK_SUPPORT_SCREEN_RECORDER` = `TRUE` - enable Advanced Screen Capture
- `SEC_FLOATING_FEATURE_FRAMEWORK_SUPPORT_SECONDARY_DISPLAY_AS_COVER` - Framework: adds secondary display as cover
- `SEC_FLOATING_FEATURE_FRAMEWORK_SUPPORT_SMART_SUGGESTIONS_WIDGET` = `TRUE` - enables the smart suggestions widget
- `SEC_FLOATING_FEATURE_FRAMEWORK_SUPPORT_SMOOTH_SCROLL` = `TRUE` - enable Smooth Scroll of Surface Flinger
- `SEC_FLOATING_FEATURE_FRAMEWORK_SUPPORT_STACK_WIDGET_AUTO_ROTATION` = `TRUE` - Framework: adds stack widget auto rotation
- `SEC_FLOATING_FEATURE_FRAMEWORK_SUPPORT_TSP_STATE_MANAGER` = `deadzone_v2,change_ratio` - Framework: adds tsp state manager
- `SEC_FLOATING_FEATURE_FRAMEWORK_SUPPORT_WM_CONTROLS_DISPLAY_SWITCH` - Framework: adds wm controls display switch

## LCD

- `SEC_FLOATING_FEATURE_LCD_CONFIG_ACL_DIMMING` = `0` - LCD: sets acl dimming
- `SEC_FLOATING_FEATURE_LCD_CONFIG_AOD_BRIGHTNESS_ANIMATION` = `1` - LCD: sets aod brightness animation
- `SEC_FLOATING_FEATURE_LCD_CONFIG_AOD_FULLSCREEN` = `1` - sets how much of the screen always on display uses
- `SEC_FLOATING_FEATURE_LCD_CONFIG_AOD_REFRESH_RATE` = `1` - LCD: sets aod refresh rate
- `SEC_FLOATING_FEATURE_LCD_CONFIG_CONTROL_AUTO_BRIGHTNESS` = `5` - LCD: sets control auto brightness
- `SEC_FLOATING_FEATURE_LCD_CONFIG_DEFAULT_SCREEN_MODE` = `4` - LCD: sets default screen mode
- `SEC_FLOATING_FEATURE_LCD_CONFIG_HFR_DEFAULT_REFRESH_RATE` = `60` - LCD: sets hfr default refresh rate
- `SEC_FLOATING_FEATURE_LCD_CONFIG_HFR_MODE` = `0` - LCD: sets hfr mode
- `SEC_FLOATING_FEATURE_LCD_CONFIG_HFR_SUPPORTED_REFRESH_RATE` = `60` - LCD: sets hfr supported refresh rate
- `SEC_FLOATING_FEATURE_LCD_CONFIG_HW_MDNIE` = `QC` - LCD: sets hw mdnie
- `SEC_FLOATING_FEATURE_LCD_CONFIG_LOCAL_HBM` = `0` - LCD: sets local hbm
- `SEC_FLOATING_FEATURE_LCD_CONFIG_NATURAL_MODE_TYPE` = `0` - LCD: sets natural mode type
- `SEC_FLOATING_FEATURE_LCD_CONFIG_NIGHT_DIM` = `1` - LCD: sets night dim
- `SEC_FLOATING_FEATURE_LCD_CONFIG_PRIVACY_DISPLAY` = `0` - LCD: sets privacy display
- `SEC_FLOATING_FEATURE_LCD_CONFIG_REDDISH_COMPENSATION` = `0` - LCD: sets reddish compensation
- `SEC_FLOATING_FEATURE_LCD_CONFIG_REPLACE_COLOR_FOR_DARKMODE` = `#FF171717` - enable darker Dark Mode
- `SEC_FLOATING_FEATURE_LCD_CONFIG_SELFMASK_VERSION` = `0` - LCD: sets selfmask version
- `SEC_FLOATING_FEATURE_LCD_CONFIG_SUB_HFR_MODE` = `0` - LCD: sets sub hfr mode
- `SEC_FLOATING_FEATURE_LCD_CONFIG_VIVIDNESS` = `1` - LCD: sets vividness
- `SEC_FLOATING_FEATURE_LCD_CONFIG_VIVIDPLUS` = `1` - LCD: sets vividplus
- `SEC_FLOATING_FEATURE_LCD_SUPPORT_AMOLED_DISPLAY` = `TRUE` - LCD: adds amoled display
- `SEC_FLOATING_FEATURE_LCD_SUPPORT_BLUE_FILTER_ADAPTIVE_MODE` = `1` - LCD: adds blue filter adaptive mode
- `SEC_FLOATING_FEATURE_LCD_SUPPORT_DETAIL_BRIGHTNESS` - LCD: adds detail brightness
- `SEC_FLOATING_FEATURE_LCD_SUPPORT_EXTRA_BRIGHTNESS` = `TRUE` - enables extra brightness, which is what outdoor mode uses
- `SEC_FLOATING_FEATURE_LCD_SUPPORT_JELLY_SCROLL_IMPROVE_SOLUTION` - LCD: adds jelly scroll improve solution
- `SEC_FLOATING_FEATURE_LCD_SUPPORT_MDNIE_HW` = `TRUE` - enable Extra Screen Modes
- `SEC_FLOATING_FEATURE_LCD_SUPPORT_NATURAL_SCREEN_MODE` - LCD: adds natural screen mode
- `SEC_FLOATING_FEATURE_LCD_SUPPORT_SCREEN_MODE_TYPE` = `0` - LCD: adds screen mode type
- `SEC_FLOATING_FEATURE_LCD_SUPPORT_SELFMASK` = `TRUE` - LCD: adds selfmask
- `SEC_FLOATING_FEATURE_LCD_SUPPORT_TOUCH_EVENT_AUTOBRIGHTNESS` - LCD: adds touch event autobrightness
- `SEC_FLOATING_FEATURE_LCD_SUPPORT_WIDE_COLOR_GAMUT` = `TRUE` - enable Extra Screen Modes

## Settings

- `SEC_FLOATING_FEATURE_SETTINGS_CONFIG_BATTERY_CAPACITY` = `0000 mAh` - change battery capacity
- `SEC_FLOATING_FEATURE_SETTINGS_CONFIG_BRAND_NAME` = `Your Choosed Name` - change Device Name to Your Choosed one
- `SEC_FLOATING_FEATURE_SETTINGS_CONFIG_DEFAULT_FONT_SIZE` = `2` - Settings: sets default font size
- `SEC_FLOATING_FEATURE_SETTINGS_CONFIG_DEFAULT_POCKET_MODE` = `1` - Settings: sets default pocket mode
- `SEC_FLOATING_FEATURE_SETTINGS_CONFIG_ELECTRIC_RATED_VALUE` = `DC 10 V; 4.5 A / DC 15 V; 3 A` - Settings: sets electric rated value
- `SEC_FLOATING_FEATURE_SETTINGS_CONFIG_FCC_ID` = `A3LSMS938U` - Settings: sets fcc id
- `SEC_FLOATING_FEATURE_SETTINGS_CONFIG_RESTORE_EXCLUDED_ITEMS` - Settings: sets restore excluded items
- `SEC_FLOATING_FEATURE_SETTINGS_CONFIG_SPEN_FCC_ID` - Settings: sets spen fcc id
- `SEC_FLOATING_FEATURE_SETTINGS_DISABLE_TRANSCODE_MTP_MENU` - Settings: turns off transcode mtp menu
- `SEC_FLOATING_FEATURE_SETTINGS_ENABLE_EU_BATTERY_REGULATORY` - Settings: enables eu battery regulatory
- `SEC_FLOATING_FEATURE_SETTINGS_ENABLE_EU_BATTERY_REGULATORY_WITHOUT_IC` - Settings: enables eu battery regulatory without ic
- `SEC_FLOATING_FEATURE_SETTINGS_SUPPORT_ACCESSORY` = `TRUE` - Settings: adds accessory
- `SEC_FLOATING_FEATURE_SETTINGS_SUPPORT_AUTO_BRIGTNESS` = `TRUE` - Settings: adds auto brigtness
- `SEC_FLOATING_FEATURE_SETTINGS_SUPPORT_AUTO_POWER_ON_OFF` = `TRUE` - adds auto power on and off to Settings
- `SEC_FLOATING_FEATURE_SETTINGS_SUPPORT_DEFAULT_DOUBLE_TAP_TO_WAKE` = `TRUE` - Settings: adds default double tap to wake
- `SEC_FLOATING_FEATURE_SETTINGS_SUPPORT_DOCK` - Settings: adds dock
- `SEC_FLOATING_FEATURE_SETTINGS_SUPPORT_EASY_MODE` = `TRUE` - Settings: adds easy mode
- `SEC_FLOATING_FEATURE_SETTINGS_SUPPORT_FUNCTION_KEY_MENU` = `TRUE` - enable Side Key Function
- `SEC_FLOATING_FEATURE_SETTINGS_SUPPORT_MOTION` = `TRUE` - Settings: adds motion
- `SEC_FLOATING_FEATURE_SETTINGS_SUPPORT_MOTION_PALM_SWIPE` = `TRUE` - Settings: adds motion palm swipe
- `SEC_FLOATING_FEATURE_SETTINGS_SUPPORT_MOTION_PALM_TOUCH` = `TRUE` - Settings: adds motion palm touch
- `SEC_FLOATING_FEATURE_SETTINGS_SUPPORT_MOTION_PICK_UP` = `TRUE` - Settings: adds motion pick up
- `SEC_FLOATING_FEATURE_SETTINGS_SUPPORT_MOTION_PICK_UP_TO_CALL_OUT` = `TRUE` - Settings: adds motion pick up to call out
- `SEC_FLOATING_FEATURE_SETTINGS_SUPPORT_MOTION_TRUN_OVER` = `TRUE` - Settings: adds motion trun over
- `SEC_FLOATING_FEATURE_SETTINGS_SUPPORT_SEPERATE_LOCK_AND_SECURITY` - Settings: adds seperate lock and security
- `SEC_FLOATING_FEATURE_SETTINGS_SUPPORT_SUW_LPP_AI_AGENT` - Settings: adds suw lpp ai agent
- `SEC_FLOATING_FEATURE_SETTINGS_SUPPORT_TOUCH_GLOVE_MATERIAL` - Settings: adds touch glove material
- `SEC_FLOATING_FEATURE_SETTINGS_SUPPORT_TOUCH_SENSTIVITY_MATERIAL` = `TRUE` - Settings: adds touch senstivity material
- `SEC_FLOATING_FEATURE_SETTINGS_SUPPORT_VARIABLE_RATED` - Settings: adds variable rated

## Fmradio

- `SEC_FLOATING_FEATURE_FMRADIO_CONFIG_AVOID_REGION` = `EUR,CIS` - Fmradio: sets avoid region
- `SEC_FLOATING_FEATURE_FMRADIO_CONFIG_CHIP_VENDOR` = `0` - Fmradio: sets chip vendor
- `SEC_FLOATING_FEATURE_FMRADIO_CONFIG_COMMON_RSSI` = `0` - Fmradio: sets common rssi
- `SEC_FLOATING_FEATURE_FMRADIO_CONFIG_COMMON_SNR` = `0` - Fmradio: sets common snr
- `SEC_FLOATING_FEATURE_FMRADIO_CONFIG_COMMON_SOFTMUTE_TH` = `0` - Fmradio: sets common softmute th
- `SEC_FLOATING_FEATURE_FMRADIO_CONFIG_MEDIATEK_BLENDPAMD_TH` = `-42` - Fmradio: sets mediatek blendpamd th
- `SEC_FLOATING_FEATURE_FMRADIO_CONFIG_MEDIATEK_BLENDRSSI_TH` = `-69` - Fmradio: sets mediatek blendrssi th
- `SEC_FLOATING_FEATURE_FMRADIO_CONFIG_MEDIATEK_CHIPVOLUME` - Fmradio: sets mediatek chipvolume
- `SEC_FLOATING_FEATURE_FMRADIO_CONFIG_MEDIATEK_DESENSE_LIST` = `0` - Fmradio: sets mediatek desense list
- `SEC_FLOATING_FEATURE_FMRADIO_CONFIG_MEDIATEK_SEEKDESENSERSSI` = `-90` - Fmradio: sets mediatek seekdesenserssi
- `SEC_FLOATING_FEATURE_FMRADIO_CONFIG_MEDIATEK_SEEKSMG` = `1` - Fmradio: sets mediatek seeksmg
- `SEC_FLOATING_FEATURE_FMRADIO_CONFIG_QUALCOMM_BLEND_RMSSI_HI` = `0` - Fmradio: sets qualcomm blend rmssi hi
- `SEC_FLOATING_FEATURE_FMRADIO_CONFIG_QUALCOMM_BLEND_SINR_HI` = `0` - Fmradio: sets qualcomm blend sinr hi
- `SEC_FLOATING_FEATURE_FMRADIO_CONFIG_QUALCOMM_GOODCH_RMSSITH` = `-110` - Fmradio: sets qualcomm goodch rmssith
- `SEC_FLOATING_FEATURE_FMRADIO_CONFIG_RICHWAVE_SEEK_DC` = `64` - Fmradio: sets richwave seek dc
- `SEC_FLOATING_FEATURE_FMRADIO_CONFIG_RICHWAVE_SEEK_QA` = `80` - Fmradio: sets richwave seek qa
- `SEC_FLOATING_FEATURE_FMRADIO_CONFIG_SLSI_BLENDCOEF` = `3172` - Fmradio: sets slsi blendcoef
- `SEC_FLOATING_FEATURE_FMRADIO_CONFIG_SLSI_IFCOUNT1` = `4800` - Fmradio: sets slsi ifcount1
- `SEC_FLOATING_FEATURE_FMRADIO_CONFIG_SLSI_IFCOUNT2` = `5600` - Fmradio: sets slsi ifcount2
- `SEC_FLOATING_FEATURE_FMRADIO_CONFIG_SOFTMUTE_PATH` = `Speaker` - Fmradio: sets softmute path
- `SEC_FLOATING_FEATURE_FMRADIO_CONFIG_SPRD_FREQ_OFFSET` = `1500` - Fmradio: sets sprd freq offset
- `SEC_FLOATING_FEATURE_FMRADIO_CONFIG_SPRD_NOISE_PWR` = `176` - Fmradio: sets sprd noise pwr
- `SEC_FLOATING_FEATURE_FMRADIO_CONFIG_SPRD_PILOT_PWR` = `400` - Fmradio: sets sprd pilot pwr
- `SEC_FLOATING_FEATURE_FMRADIO_SUPPORT_EXTERNAL_RADIO_CHIPSET` - Fmradio: adds external radio chipset
- `SEC_FLOATING_FEATURE_FMRADIO_SUPPORT_INDIRECT_MODE` - Fmradio: adds indirect mode
- `SEC_FLOATING_FEATURE_FMRADIO_SUPPORT_RDS` = `TRUE` - Fmradio: adds rds
- `SEC_FLOATING_FEATURE_FMRADIO_SUPPORT_SOFTMUTE` = `TRUE` - Fmradio: adds softmute

## MMFW

- `SEC_FLOATING_FEATURE_MMFW_CONFIG_MEDIA_CONTEXT_ANALYZER_CORE` = `NPU` - MMFW: sets media context analyzer core
- `SEC_FLOATING_FEATURE_MMFW_CONFIG_UHDA` - MMFW: sets uhda
- `SEC_FLOATING_FEATURE_MMFW_SUPPORT_AC4_CODEC` = `TRUE` - MMFW: adds ac4 codec
- `SEC_FLOATING_FEATURE_MMFW_SUPPORT_APE_FORMAT` = `TRUE` - MMFW: adds ape format
- `SEC_FLOATING_FEATURE_MMFW_SUPPORT_DOLBY_AUDIO` = `TRUE` - MMFW: adds dolby audio
- `SEC_FLOATING_FEATURE_MMFW_SUPPORT_DSD_FORMAT` = `TRUE` - MMFW: adds dsd format
- `SEC_FLOATING_FEATURE_MMFW_SUPPORT_HDR10PLUS_PLAYBACK` - MMFW: adds hdr10 plus playback
- `SEC_FLOATING_FEATURE_MMFW_SUPPORT_HDR2SDR` = `TRUE` - MMFW: adds hdr2 sdr
- `SEC_FLOATING_FEATURE_MMFW_SUPPORT_HDR2SDR_MAX_8K` = `TRUE` - MMFW: adds hdr2 sdr max 8 k
- `SEC_FLOATING_FEATURE_MMFW_SUPPORT_HDR_2_SDR` - MMFW: adds hdr 2 sdr
- `SEC_FLOATING_FEATURE_MMFW_SUPPORT_HIERARCHICAL_B_ENCODING` = `TRUE` - MMFW: adds hierarchical b encoding
- `SEC_FLOATING_FEATURE_MMFW_SUPPORT_HW_HDR` - MMFW: adds hw hdr
- `SEC_FLOATING_FEATURE_MMFW_SUPPORT_LONGEXPOSURE_EFFECT` = `TRUE` - MMFW: adds longexposure effect
- `SEC_FLOATING_FEATURE_MMFW_SUPPORT_LONGEXPOSURE_EFFECT_10BIT` = `TRUE` - MMFW: adds longexposure effect 10 bit
- `SEC_FLOATING_FEATURE_MMFW_SUPPORT_MEDIA_CONTEXT_ANALYZER` = `TRUE` - MMFW: adds media context analyzer
- `SEC_FLOATING_FEATURE_MMFW_SUPPORT_MHDRSERVICE` - MMFW: adds mhdrservice
- `SEC_FLOATING_FEATURE_MMFW_SUPPORT_MHDRSERVICE_BRIGHTNESS_CONTROL` - MMFW: adds mhdrservice brightness control
- `SEC_FLOATING_FEATURE_MMFW_SUPPORT_MTK_SSM_SM_VIDEO` - MMFW: adds mtk ssm sm video
- `SEC_FLOATING_FEATURE_MMFW_SUPPORT_MULTI_VIEW` - MMFW: adds multi view
- `SEC_FLOATING_FEATURE_MMFW_SUPPORT_MUSIC_ALBUMART_3DAUDIO` = `TRUE` - MMFW: adds music albumart 3 daudio
- `SEC_FLOATING_FEATURE_MMFW_SUPPORT_PHOTOHDR` = `TRUE` - MMFW: adds photohdr
- `SEC_FLOATING_FEATURE_MMFW_SUPPORT_SLOWMOTION_V2` - MMFW: adds slowmotion v2
- `SEC_FLOATING_FEATURE_MMFW_SUPPORT_SLOWMOTION_V2_120FPS` - MMFW: adds slowmotion v2 120 fps
- `SEC_FLOATING_FEATURE_MMFW_SUPPORT_SLOWMOTION_V2_NO_SVC` - MMFW: adds slowmotion v2 no svc
- `SEC_FLOATING_FEATURE_MMFW_SUPPORT_TARGET_TRACKING` = `TRUE` - MMFW: adds target tracking
- `SEC_FLOATING_FEATURE_MMFW_SUPPORT_VIDEOSERACH` - MMFW: adds videoserach
- `SEC_FLOATING_FEATURE_MMFW_UNSUPPORT_TRANSCODE_8K10BIT` - MMFW: unsupport transcode 8 k10 bit

## Battery

- `SEC_FLOATING_FEATURE_BATTERY_DISABLE_ECO_BATTERY` - Battery: turns off eco battery
- `SEC_FLOATING_FEATURE_BATTERY_DISABLE_ECO_BATTERY_FEATURE` - Battery: turns off eco battery feature
- `SEC_FLOATING_FEATURE_BATTERY_SUPPORT_BSOH_GALAXYDIAGNOSTICS` = `TRUE` - adds battery health to Galaxy Diagnostics
- `SEC_FLOATING_FEATURE_BATTERY_SUPPORT_BSOH_SETTINGS` = `TRUE` - adds battery health to Settings
- `SEC_FLOATING_FEATURE_BATTERY_SUPPORT_HV` = `TRUE` - enable Wireless PowerShare
- `SEC_FLOATING_FEATURE_BATTERY_SUPPORT_HV_DURING_CHARGING` = `TRUE` - Battery: adds hv during charging
- `SEC_FLOATING_FEATURE_BATTERY_SUPPORT_LONGLIFE_FORCE_CUTOFF` = `TRUE` - Battery: adds longlife force cutoff
- `SEC_FLOATING_FEATURE_BATTERY_SUPPORT_LONGLIFE_OPTION` - Battery: adds longlife option
- `SEC_FLOATING_FEATURE_BATTERY_SUPPORT_PASS_THROUGH` = `TRUE` - enables pass through charging
- `SEC_FLOATING_FEATURE_BATTERY_SUPPORT_PD_HV` - Battery: adds pd hv
- `SEC_FLOATING_FEATURE_BATTERY_SUPPORT_SBP_INFO_SETTINGS` - Battery: adds sbp info settings
- `SEC_FLOATING_FEATURE_BATTERY_SUPPORT_WIRELESS_HV` = `TRUE` - enable Wireless PowerShare
- `SEC_FLOATING_FEATURE_BATTERY_SUPPORT_WIRELESS_NIGHT_MODE` = `TRUE` - enable Wireless PowerShare
- `SEC_FLOATING_FEATURE_BATTERY_SUPPORT_WIRELESS_TX` = `TRUE` - enables wireless power sharing

## Gallery

- `SEC_FLOATING_FEATURE_GALLERY_CONFIG_AI_EXPANSION` = `AI_Timelapse,singletake.hidt.support.on,singletake.capture.support.off,singletake.video_res.config.fhd,singletake.video.previous_record` - Gallery: sets ai expansion
- `SEC_FLOATING_FEATURE_GALLERY_CONFIG_BEST_FACE_MODE` = `GENIMAGE` - Gallery: sets best face mode
- `SEC_FLOATING_FEATURE_GALLERY_CONFIG_FACE_CLUSTER_VERSION` = `SR_V7` - Gallery: sets face cluster version
- `SEC_FLOATING_FEATURE_GALLERY_CONFIG_IMAGE_TAGGER_UPDATE` = `None` - Gallery: sets image tagger update
- `SEC_FLOATING_FEATURE_GALLERY_CONFIG_IMAGE_TAGGER_VERSION` = `V1101` - Gallery: sets image tagger version
- `SEC_FLOATING_FEATURE_GALLERY_CONFIG_LIVEFOCUS_EFFECT_DUAL_BOKEH` = `BLUR,EFFECT,BIGBOKEH,PORTRAIT,RELIGHT,REFOCUS,LIGHT360,GENERIC_REFOCUS,GENERIC_REEDIT` - Gallery: sets livefocus effect dual bokeh
- `SEC_FLOATING_FEATURE_GALLERY_CONFIG_PBE` = `TRUE` - Gallery: sets pbe
- `SEC_FLOATING_FEATURE_GALLERY_CONFIG_PET_CLUSTER_VERSION` = `V1001` - Gallery: sets pet cluster version
- `SEC_FLOATING_FEATURE_GALLERY_CONFIG_ZOOM_TYPE` = `ZOOM_2K` - Gallery: sets zoom type
- `SEC_FLOATING_FEATURE_GALLERY_SUPPORT_GO_TO_URL` - Gallery: adds go to url
- `SEC_FLOATING_FEATURE_GALLERY_SUPPORT_LOG_CORRECT_COLOR` = `TRUE` - Gallery: adds log correct color
- `SEC_FLOATING_FEATURE_GALLERY_SUPPORT_SINGLE_SHOT_ONLY` - Gallery: adds single shot only
- `SEC_FLOATING_FEATURE_GALLERY_SUPPORT_SPC_LOCATION_POI` = `TRUE` - Gallery: adds spc location poi
- `SEC_FLOATING_FEATURE_GALLERY_SUPPORT_STORYEDITOR` = `0` - Gallery: adds storyeditor

## Graphics

- `SEC_FLOATING_FEATURE_GRAPHICS_CONFIG_GAMEBOOSTER_MORE_HEAT` = `30` - Graphics: sets gamebooster more heat
- `SEC_FLOATING_FEATURE_GRAPHICS_CONFIG_GAMEBOOSTER_SUICIDE_INTERVAL_MS` = `180000` - Graphics: sets gamebooster suicide interval ms
- `SEC_FLOATING_FEATURE_GRAPHICS_CONFIG_GAME_DEFAULT_FRAMERATE` = `120` - Graphics: sets game default framerate
- `SEC_FLOATING_FEATURE_GRAPHICS_SUPPORT_3D_SURFACE_TRANSITION_FLAG` = `TRUE` - enable Drawer Clearer Contrast
- `SEC_FLOATING_FEATURE_GRAPHICS_SUPPORT_CAPTURED_BLUR` = `TRUE` - enable Semi Native Blur
- `SEC_FLOATING_FEATURE_GRAPHICS_SUPPORT_DEFAULT_GAMELAUNCHER_ENABLE` = `TRUE` - enable Game Launcher in Drawer
- `SEC_FLOATING_FEATURE_GRAPHICS_SUPPORT_DPU_READBACK` - Graphics: adds dpu readback
- `SEC_FLOATING_FEATURE_GRAPHICS_SUPPORT_GAMEBOOSTER_MANUAL_ROUTINE` = `TRUE` - Graphics: adds gamebooster manual routine
- `SEC_FLOATING_FEATURE_GRAPHICS_SUPPORT_GAMEBOOSTER_PERF_MONITOR` = `TRUE` - Graphics: adds gamebooster perf monitor
- `SEC_FLOATING_FEATURE_GRAPHICS_SUPPORT_GAME_SERVER_POLICY_QUERIES` = `TRUE` - Graphics: adds game server policy queries
- `SEC_FLOATING_FEATURE_GRAPHICS_SUPPORT_PARTIAL_BLUR` = `TRUE` - enable Partial Blur
- `SEC_FLOATING_FEATURE_GRAPHICS_SUPPORT_REDUCE_FLASH_LIGHT` = `TRUE` - Graphics: adds reduce flash light
- `SEC_FLOATING_FEATURE_GRAPHICS_SUPPORT_RELUMINO_EFFECT_FLAG` = `TRUE` - Graphics: adds relumino effect flag
- `SEC_FLOATING_FEATURE_GRAPHICS_SUPPORT_TOUCH_FAST_RESPONSE` = `TRUE` - enables the high touch sampling rate

## Genai

- `SEC_FLOATING_FEATURE_GENAI_CONFIG_FOUNDATION_MODEL` = `3B` - Genai: sets foundation model
- `SEC_FLOATING_FEATURE_GENAI_CONFIG_LLM_VERSION` = `0.81` - Genai: sets llm version
- `SEC_FLOATING_FEATURE_GENAI_SUPPORT_C2PA` = `TRUE` - Genai: adds c2 pa
- `SEC_FLOATING_FEATURE_GENAI_SUPPORT_IMAGE_CLIPPER` = `TRUE` - Genai: adds image clipper
- `SEC_FLOATING_FEATURE_GENAI_SUPPORT_OBJECT_ERASER` = `TRUE` - Genai: adds object eraser
- `SEC_FLOATING_FEATURE_GENAI_SUPPORT_OFFLINE_LANGUAGEMODEL` = `TRUE` - enables the on-device language model
- `SEC_FLOATING_FEATURE_GENAI_SUPPORT_REFLECTION_ERASER` = `TRUE` - Genai: adds reflection eraser
- `SEC_FLOATING_FEATURE_GENAI_SUPPORT_SHADOW_ERASER` = `TRUE` - Genai: adds shadow eraser
- `SEC_FLOATING_FEATURE_GENAI_SUPPORT_SMART_LASSO` = `TRUE` - Genai: adds smart lasso
- `SEC_FLOATING_FEATURE_GENAI_SUPPORT_SPOT_FIXER` = `TRUE` - Genai: adds spot fixer
- `SEC_FLOATING_FEATURE_GENAI_SUPPORT_STYLE_TRANSFER` = `TRUE` - Genai: adds style transfer
- `SEC_FLOATING_FEATURE_GENAI_SUPPORT_TIME_WEATHER_WALLPAPER` = `V2` - Genai: adds time weather wallpaper

## Bixby

- `SEC_FLOATING_FEATURE_BIXBY_CONFIG_BARGEIN_FUNCTION` = `0` - Bixby: sets bargein function
- `SEC_FLOATING_FEATURE_BIXBY_CONFIG_BARGEIN_PARAM_MODE` = `2` - Bixby: sets bargein param mode
- `SEC_FLOATING_FEATURE_BIXBY_CONFIG_CUSTOM_FIRMWARE` = `2` - Bixby: sets custom firmware
- `SEC_FLOATING_FEATURE_BIXBY_CONFIG_DSPNS_FUNCTION` = `0` - Bixby: sets dspns function
- `SEC_FLOATING_FEATURE_BIXBY_CONFIG_DSP_BITRATE` = `32bit` - Bixby: sets dsp bitrate
- `SEC_FLOATING_FEATURE_BIXBY_CONFIG_HWKEY` - Bixby: sets hwkey
- `SEC_FLOATING_FEATURE_BIXBY_SUPPORT_BIXBYKWD` = `TRUE` - enables Bixby wake word detection
- `SEC_FLOATING_FEATURE_BIXBY_SUPPORT_CUSTOM_WAKEUP` = `2` - Bixby: adds custom wakeup
- `SEC_FLOATING_FEATURE_BIXBY_SUPPORT_FARFIELD_WAKEUP` - Bixby: adds farfield wakeup
- `SEC_FLOATING_FEATURE_BIXBY_SUPPORT_LONG_KEY_SERVICE` = `TRUE` - enables the long press Bixby service
- `SEC_FLOATING_FEATURE_BIXBY_SUPPORT_SANXINGXIAOBEIKWD` = `TRUE` - enables the Chinese Bixby wake word

## SIP

- `SEC_FLOATING_FEATURE_SIP_CONFIG_ADDTIONAL_INPUT_METHOD` - SIP: sets addtional input method
- `SEC_FLOATING_FEATURE_SIP_CONFIG_ENGINE_DB_TYPE` = `ALM` - SIP: sets engine db type
- `SEC_FLOATING_FEATURE_SIP_CONFIG_FOLD_UX_VERSION` = `0` - SIP: sets fold ux version
- `SEC_FLOATING_FEATURE_SIP_CONFIG_HWR_ENGINE` = `SSHWRPANEL` - SIP: sets hwr engine
- `SEC_FLOATING_FEATURE_SIP_CONFIG_PACKAGE_NAME` = `com.samsung.android.honeyboard` - SIP: sets package name
- `SEC_FLOATING_FEATURE_SIP_CONFIG_PREDICTION_ENGINE` = `XT9` - SIP: sets prediction engine
- `SEC_FLOATING_FEATURE_SIP_ENABLE_DEF_KEY_SOUND` = `TRUE` - SIP: enables def key sound
- `SEC_FLOATING_FEATURE_SIP_SUPPORT_CURSOR_CONTROL` = `TRUE` - SIP: adds cursor control
- `SEC_FLOATING_FEATURE_SIP_SUPPORT_DIRECT_WRITING_ENABLE` - SIP: adds direct writing enable
- `SEC_FLOATING_FEATURE_SIP_SUPPORT_EMOJI_SHORTCUT` - SIP: adds emoji shortcut

## SAIV

- `SEC_FLOATING_FEATURE_SAIV_CONFIG_AI_REVITAL_VERSION` = `1.9,3` - SAIV: sets ai revital version
- `SEC_FLOATING_FEATURE_SAIV_CONFIG_ARDOODLE_LIB` = `PET_DETECTION,IMG_PICKING` - SAIV: sets ardoodle lib
- `SEC_FLOATING_FEATURE_SAIV_CONFIG_BEAUTY_FACE` - SAIV: sets beauty face
- `SEC_FLOATING_FEATURE_SAIV_CONFIG_MIDAS` = `UPSCALE,UPSCALE_PRO,UPSCALE_ULTRA,LOWLIGHT,HDR,DEBLUR,MOIRE,DENOISE,SHADOW,REFLECTION,UWDC,FLARE,FACERESTORATION` - SAIV: sets midas
- `SEC_FLOATING_FEATURE_SAIV_SUPPORT_3DPHOTO` = `TRUE` - SAIV: adds 3 dphoto
- `SEC_FLOATING_FEATURE_SAIV_SUPPORT_3DPHOTO_VIEW` - SAIV: adds 3 dphoto view
- `SEC_FLOATING_FEATURE_SAIV_SUPPORT_AI_REVITAL` = `TRUE` - SAIV: adds ai revital
- `SEC_FLOATING_FEATURE_SAIV_SUPPORT_BEAUTY_LITE` - SAIV: adds beauty lite

## Lockscreen

- `SEC_FLOATING_FEATURE_LOCKSCREEN_CONFIG_DEFAULT_WALLPAPER_STYLE` - Lockscreen: sets default wallpaper style
- `SEC_FLOATING_FEATURE_LOCKSCREEN_CONFIG_DEFAULT_WALLPAPER_STYLE_SUB` - Lockscreen: sets default wallpaper style sub
- `SEC_FLOATING_FEATURE_LOCKSCREEN_CONFIG_POLICY_LIST` - Lockscreen: sets policy list
- `SEC_FLOATING_FEATURE_LOCKSCREEN_CONFIG_PUNCHHOLE_VI` = `face,pos:0.5:0.0213,size:0.0777:0.0359,type:circle` - Lockscreen: sets punchhole vi
- `SEC_FLOATING_FEATURE_LOCKSCREEN_CONFIG_SUBDISPLAY_POLICY` - Lockscreen: sets subdisplay policy
- `SEC_FLOATING_FEATURE_LOCKSCREEN_CONFIG_WALLPAPER_COLOR_REGION` - Lockscreen: sets wallpaper color region
- `SEC_FLOATING_FEATURE_LOCKSCREEN_CONFIG_WALLPAPER_STYLE` = `VIDEO,GENWEATHER,FLIPSUIT_LOCK` - Lockscreen: sets wallpaper style

## System

- `SEC_FLOATING_FEATURE_SYSTEM_CONFIG_HCM_AI_POWER_SAVING_LEVEL` = `225` - System: sets hcm ai power saving level
- `SEC_FLOATING_FEATURE_SYSTEM_CONFIG_SIOP_POLICY_FILENAME` = `siop_pa3q_sm8750` - System: sets siop policy filename
- `SEC_FLOATING_FEATURE_SYSTEM_SUPPORT_ENHANCED_CPU_RESPONSIVENESS` = `TRUE` - enables enhanced CPU responsiveness
- `SEC_FLOATING_FEATURE_SYSTEM_SUPPORT_ENHANCED_PROCESSING` = `TRUE` - enables enhanced processing
- `SEC_FLOATING_FEATURE_SYSTEM_SUPPORT_LOW_HEAT_MODE` = `TRUE` - enables low heat mode
- `SEC_FLOATING_FEATURE_SYSTEM_SUPPORT_ROLE_SWAP_DISABLE` - System: adds role swap disable
- `SEC_FLOATING_FEATURE_SYSTEM_SUPPORT_SCREEN_CURTAIN` = `TRUE` - enables screen curtain

## Systemui

- `SEC_FLOATING_FEATURE_SYSTEMUI_CONFIG_CORNER_ROUND` = `0` - enable custom values for Status Bar and QS panel
- `SEC_FLOATING_FEATURE_SYSTEMUI_CONFIG_EDGELIGHTING_FRAME_EFFECT` = `frame_effect` - enable Flagship Edge Ligthining+ Animations in R
- `SEC_FLOATING_FEATURE_SYSTEMUI_CONFIG_NOTIFICATION_BG_COLOR` = `0` - enable custom values for Status Bar and QS panel
- `SEC_FLOATING_FEATURE_SYSTEMUI_CONFIG_NOTIFICATION_ICON_SIZE` = `0` - enable custom values for Status Bar and QS panel
- `SEC_FLOATING_FEATURE_SYSTEMUI_CONFIG_SHOW_CONTENT_WHEN_UNLOCKED` = `support;defaulton` - Systemui: sets show content when unlocked
- `SEC_FLOATING_FEATURE_SYSTEMUI_CONFIG_STATUSBAR_SIDE_PADDING` = `0` - enable custom values for Status Bar and QS panel
- `SEC_FLOATING_FEATURE_SYSTEMUI_SUPPORT_BRIEF_NOTIFICATION` = `TRUE` - enables the brief notification style

## Vision

- `SEC_FLOATING_FEATURE_VISION_CONFIG_FACE_DETECTOR_SOLUTION` = `SW` - Vision: sets face detector solution
- `SEC_FLOATING_FEATURE_VISION_CONFIG_IMAGE_CROPPER_VERSION` = `V1` - Vision: sets image cropper version
- `SEC_FLOATING_FEATURE_VISION_CONFIG_IMAGE_TRANSLATION_OVERLAY_VERSION` = `5` - Vision: sets image translation overlay version
- `SEC_FLOATING_FEATURE_VISION_CONFIG_RELIGHTING_SOLUTION` = `arcsoft.v1` - Vision: sets relighting solution
- `SEC_FLOATING_FEATURE_VISION_CONFIG_STORYGEN` = `RECAP` - Vision: sets storygen
- `SEC_FLOATING_FEATURE_VISION_SUPPORT_AI_MY_FAVORITE_CONTENTS` = `TRUE` - enables AI favourite content

## Accessibility

- `SEC_FLOATING_FEATURE_ACCESSIBILITY_SUPPORT_AI_CORE_IMAGE_DESCRIPTION` = `TRUE` - Accessibility: adds ai core image description
- `SEC_FLOATING_FEATURE_ACCESSIBILITY_SUPPORT_ALLOW_SERVICES` = `TRUE` - Accessibility: adds allow services
- `SEC_FLOATING_FEATURE_ACCESSIBILITY_SUPPORT_HEARING_AIDS` = `TRUE` - Accessibility: adds hearing aids
- `SEC_FLOATING_FEATURE_ACCESSIBILITY_SUPPORT_MANAGE_ACCESSIBILITY` - Accessibility: adds manage accessibility
- `SEC_FLOATING_FEATURE_ACCESSIBILITY_SUPPORT_MANAGE_EXCLUSIVE_TASK` = `TRUE` - Accessibility: adds manage exclusive task

## Launcher

- `SEC_FLOATING_FEATURE_LAUNCHER_CONFIG_ANIMATION_TYPE` = `HighEnd` - enable Flagship Launcher Animations
- `SEC_FLOATING_FEATURE_LAUNCHER_CONFIG_LOCAL_THEME_DOWNLOAD` = `China` - Launcher: sets local theme download
- `SEC_FLOATING_FEATURE_LAUNCHER_CONFIG_ZERO_PAGE_PACKAGE_NAMES` = `com.google.android.googlequicksearchbox` - enable Google Discover in Drawer
- `SEC_FLOATING_FEATURE_LAUNCHER_SUPPORT_CLOCK_LIVE_ICON` = `TRUE` - enable Live Clock in Launcher
- `SEC_FLOATING_FEATURE_LAUNCHER_SUPPORT_TASKBAR` - Launcher: adds taskbar

## Clock

- `SEC_FLOATING_FEATURE_CLOCK_CONFIG_ALARM_SOUND` = `spotify` - enable Spotify as added alarm
- `SEC_FLOATING_FEATURE_CLOCK_CONFIG_PACKAGE_NAME` = `com.sec.android.app.clockpackage` - Clock: sets package name
- `SEC_FLOATING_FEATURE_CLOCK_SUPPORT_PREMIUM_WATCH` - Clock: adds premium watch

## Factory

- `SEC_FLOATING_FEATURE_FACTORY_CONFIG_PART_REPLACEMENT_HISTORY` = `prh` - Factory: sets part replacement history
- `SEC_FLOATING_FEATURE_FACTORY_SUPPORT_FTL_SPEN_TYPE` = `none` - Factory: adds ftl spen type
- `SEC_FLOATING_FEATURE_FACTORY_SUPPORT_FTL_UI_RATIO` = `1.0` - Factory: adds ftl ui ratio

## Contacts

- `SEC_FLOATING_FEATURE_CONTACTS_CONFIG_PACKAGE_NAME` = `com.samsung.android.app.contacts` - Contacts: sets package name
- `SEC_FLOATING_FEATURE_CONTACTS_SUPPORT_INDEX_SCROLL` = `FALSE` - disable Index Scroll

## GPS

- `SEC_FLOATING_FEATURE_GPS_CONFIG_FOLD_CALIBRATED` = `0` - GPS: sets fold calibrated
- `SEC_FLOATING_FEATURE_GPS_CONFIG_SUPL_VENDOR` = `0` - GPS: sets supl vendor

## IMS

- `SEC_FLOATING_FEATURE_IMS_CONFIG_EVS_MAX_HW_BANDWIDTH` = `swb` - IMS: sets evs max hw bandwidth
- `SEC_FLOATING_FEATURE_IMS_SUPPORT_UPDATABLE_IMS_SERVICE` = `TRUE` - IMS: adds updatable ims service

## MCF

- `SEC_FLOATING_FEATURE_MCF_SUPPORT_CONTINUITY` = `15` - MCF: adds continuity
- `SEC_FLOATING_FEATURE_MCF_SUPPORT_FRAMEWORK` = `TRUE` - MCF: adds framework

## Message

- `SEC_FLOATING_FEATURE_MESSAGE_CONFIG_PACKAGE_NAME` = `com.samsung.android.messaging` - Message: sets package name
- `SEC_FLOATING_FEATURE_MESSAGE_CONFIG_SATELLITE_ANTHENA_PEAK` = `-0.150384, 0.086824, 0.984808` - Message: sets satellite anthena peak

## Quickconnect

- `SEC_FLOATING_FEATURE_QUICKCONNECT_CONFIG_PACKAGE_NAME` = `com.samsung.android.oneconnect` - Quickconnect: sets package name
- `SEC_FLOATING_FEATURE_QUICKCONNECT_SUPPORT_D2D` = `TRUE` - Quickconnect: adds d2 d

## Security

- `SEC_FLOATING_FEATURE_SECURITY_CONFIG_DEVICEMONITOR_PACKAGE_NAME` = `com.samsung.android.sm.devicesecurity.tcm` - changes which device monitor package is used
- `SEC_FLOATING_FEATURE_SECURITY_SUPPORT_KNOX_MATRIX_AI_PRIVACY` - Security: adds knox matrix ai privacy

## Smart

- `SEC_FLOATING_FEATURE_SMART_MANAGER` - Smart: manager
- `SEC_FLOATING_FEATURE_SMART_VIEW_APP_CAST_SUPPORTED` = `TRUE` - Smart: view app cast supported

## Voicecall

- `SEC_FLOATING_FEATURE_VOICECALL_CONFIG_INCALLUI_PACKAGE_NAME` = `com.samsung.android.incallui` - Voicecall: sets incallui package name
- `SEC_FLOATING_FEATURE_VOICECALL_SUPPORT_GLOBAL_NETWORK` = `TRUE` - Voicecall: adds global network

## Voicerecorder

- `SEC_FLOATING_FEATURE_VOICERECORDER_CONFIG_DEF_MODE` = `normal,interview,voicememo` - Voicerecorder: sets def mode
- `SEC_FLOATING_FEATURE_VOICERECORDER_CONFIG_PACKAGE_NAME` = `com.sec.android.app.voicenote` - Voicerecorder: sets package name

## Allshare

- `SEC_FLOATING_FEATURE_ALLSHARE_CONFIG_VERSION` = `DMC_ONLY` - Allshare: sets version

## Bioauth

- `SEC_FLOATING_FEATURE_BIOAUTH_CONFIG_FINGERPRINT_FEATURES` = `ultrasonic_display_phone` - Bioauth: sets fingerprint features

## Bixbyvision

- `SEC_FLOATING_FEATURE_BIXBYVISION_CONFIG_QUICKMEASURE` = `10;0.0065;1` - Bixbyvision: sets quickmeasure

## Browser

- `SEC_FLOATING_FEATURE_BROWSER_CONFIG_FAKE_MODEL_NAME` - Browser: sets fake model name

## Calendar

- `SEC_FLOATING_FEATURE_CALENDAR_CONFIG_PACKAGE_NAME` = `com.samsung.android.calendar` - Calendar: sets package name

## Contextservice

- `SEC_FLOATING_FEATURE_CONTEXTSERVICE_ENABLE_SURVEY_MODE` = `TRUE` - Contextservice: enables survey mode

## DWB

- `SEC_FLOATING_FEATURE_DWB_CONFIG_UNSUSPENDABLE_PACKAGE_NAME` = `com.android.settings;com.android.vending;com.samsung.android.dialer;com.skt.prod.dialer;com.sec.android.app.clockpackage;com.samsung.knox.securefolder;com.samsung.android.app.watchmanager;com.samsung.android.app.watchmanager2;com.samsung.android.waterpluin;com.samsung.android.minormode` - DWB: sets unsuspendable package name

## Display

- `SEC_FLOATING_FEATURE_DISPLAY_SWITCH` - Display: switch

## Drawing

- `SEC_FLOATING_FEATURE_DRAWING_ASSIST_VERSION_THRESHOLD` - Drawing: assist version threshold

## GMS

- `SEC_FLOATING_FEATURE_GMS_CONFIG_PERMISSION_PREGRANT_POLICY_LIST` - GMS: sets permission pregrant policy list

## HWR

- `SEC_FLOATING_FEATURE_HWR_CONFIG_RECOGNITION_SUPPORT` = `0` - HWR: sets recognition support

## MSCH

- `SEC_FLOATING_FEATURE_MSCH_SUPPORT_NLSEARCH` = `TRUE` - MSCH: adds nlsearch

## Prefix

- `SEC_FLOATING_FEATURE_PREFIX` - Prefix

## RIL

- `SEC_FLOATING_FEATURE_RIL_CONFIG_DM_OPERATOR` = `0` - RIL: sets dm operator

## SMP

- `SEC_FLOATING_FEATURE_SMP_CONFIG_SPP_ACTIVATION_MODE` - SMP: sets spp activation mode

## SPAY

- `SEC_FLOATING_FEATURE_SPAY_CONFIG_SWIPEUP_HEIGHT` = `0.5` - SPAY: sets swipeup height

## SPP

- `SEC_FLOATING_FEATURE_SPP_FORCE_ACTIVATION_MODE` - SPP: forces activation mode

## Samsung

- `SEC_FLOATING_FEATURE_SAMSUNG_SEARCH_SEMANTIC_SEARCH_VERSION` = `550` - Samsung: search semantic search version

## Samsungcloud

- `SEC_FLOATING_FEATURE_SAMSUNGCLOUD_SUPPORT_CONTENT_SYNC` - Samsungcloud: adds content sync

## Sensor

- `SEC_FLOATING_FEATURE_SENSOR_SUPPORT_SABC_LITE` - Sensor: adds sabc lite

## Setupwizard

- `SEC_FLOATING_FEATURE_SETUPWIZARD_CONFIG_VALUES` = `is_se_device=true` - Setupwizard: sets values

## Sfinder

- `SEC_FLOATING_FEATURE_SFINDER_CONFIG_QUERY_PARSER_VERSION` = `2` - Sfinder: sets query parser version

## Smartmanager

- `SEC_FLOATING_FEATURE_SMARTMANAGER_CONFIG_PACKAGE_NAME` = `com.samsung.android.sm_cn` - changes which Smart Manager package is used

## Support

- `SEC_FLOATING_FEATURE_SUPPORT_SINGLETAKE` - Support: singletake

## TYPE

- `SEC_FLOATING_FEATURE_TYPE_FOLD` - TYPE: fold

## Video

- `SEC_FLOATING_FEATURE_VIDEO_CONFIG_VIDEO_CLIPPING_MODE` = `NPU,unifiedclipper` - Video: sets video clipping mode

## Videoplayer

- `SEC_FLOATING_FEATURE_VIDEOPLAYER_CONFIG_PLAY_DEBOUNCE_MILLIS` - Videoplayer: sets play debounce millis

## WIFI

- `SEC_FLOATING_FEATURE_WIFI_SUPPORT_ADPS` = `TRUE` - enables Wi-Fi power saving

## WLAN

- `SEC_FLOATING_FEATURE_WLAN_SUPPORT_SECURE_WIFI` - turns Secure Wi-Fi off
