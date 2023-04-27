from pytube import YouTube
import csv


urls = []
with open("videos.csv", newline="") as f:
    reader = csv.reader(f)
    urls = [row[0] for row in reader]

for url in urls[:3]:
    yt = YouTube(url)
    print(yt.description)
    print()

# my_dict = {
#     "videoId": "CCGsMTzUkWM",
#     "thumbnail": {
#         "thumbnails": [
#             {
#                 "url": "https://i.ytimg.com/vi/CCGsMTzUkWM/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLClfIGW_FrvYGc6Ae3G0NmoXC3GHQ",
#                 "width": 168,
#                 "height": 94,
#             },
#             {
#                 "url": "https://i.ytimg.com/vi/CCGsMTzUkWM/hqdefault.jpg?sqp=-oaymwEbCMQBEG5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLCR3LBdbi0Jb9JimfqmBl7zRXNeMw",
#                 "width": 196,
#                 "height": 110,
#             },
#             {
#                 "url": "https://i.ytimg.com/vi/CCGsMTzUkWM/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLASCeELZBwuQPff_ticRfezAIN-_A",
#                 "width": 246,
#                 "height": 138,
#             },
#             {
#                 "url": "https://i.ytimg.com/vi/CCGsMTzUkWM/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLA1Tgze64K6td3IUA-OnUz6toXsgw",
#                 "width": 336,
#                 "height": 188,
#             },
#         ]
#     },
#     "title": {
#         "runs": [{"text": "HMLTD - The Worm ALBUM REVIEW"}],
#         "accessibility": {
#             "accessibilityData": {
#                 "label": "HMLTD - The Worm ALBUM REVIEW by theneedledrop 21 hours ago 5 minutes, 44 seconds 36,595 views"
#             }
#         },
#     },
#     "descriptionSnippet": {
#         "runs": [
#             {
#                 "text": "Listen: https://hmltd.bandcamp.com/album/the-worm\n\nThe songwriting and performances on The Worm are kind of an iffy foundation for HMLTD's conceptual and stylistic ambitions.\n\nMore rock reviews:..."
#             }
#         ]
#     },
#     "publishedTimeText": {"simpleText": "21 hours ago"},
#     "lengthText": {
#         "accessibility": {"accessibilityData": {"label": "5 minutes, 44 seconds"}},
#         "simpleText": "5:44",
#     },
#     "viewCountText": {"simpleText": "36,595 views"},
#     "navigationEndpoint": {
#         "clickTrackingParams": "CMwBENwwIhMI0KHxvvjI_gIVaAtPCB0mcAuDWhhVQ3Q3ZndBaFhEeTNvTkZUQXpGMm84UHeaAQYQ8jgY4AeqARpVVUxGdDdmd0FoWER5M29ORlRBekYybzhQdw==",
#         "commandMetadata": {
#             "webCommandMetadata": {
#                 "url": "/watch?v=CCGsMTzUkWM",
#                 "webPageType": "WEB_PAGE_TYPE_WATCH",
#                 "rootVe": 3832,
#             }
#         },
#         "watchEndpoint": {
#             "videoId": "CCGsMTzUkWM",
#             "watchEndpointSupportedOnesieConfig": {
#                 "html5PlaybackOnesieConfig": {
#                     "commonConfig": {
#                         "url": "https://rr2---sn-5uaeznlz.googlevideo.com/initplayback?source=youtube&oeis=1&c=WEB&oad=3200&ovd=3200&oaad=11000&oavd=11000&ocs=700&oewis=1&oputc=1&ofpcc=1&msp=1&odepv=1&id=0821ac313cd49163&ip=98.251.104.56&initcwndbps=1405000&mt=1682559189&oweuc="
#                     }
#                 }
#             },
#         },
#     },
#     "ownerBadges": [
#         {
#             "metadataBadgeRenderer": {
#                 "icon": {"iconType": "CHECK_CIRCLE_THICK"},
#                 "style": "BADGE_STYLE_TYPE_VERIFIED",
#                 "tooltip": "Verified",
#                 "trackingParams": "CMwBENwwIhMI0KHxvvjI_gIVaAtPCB0mcAuD",
#                 "accessibilityData": {"label": "Verified"},
#             }
#         }
#     ],
#     "trackingParams": "CMwBENwwIhMI0KHxvvjI_gIVaAtPCB0mcAuDQOOi0uaThuuQCKoBGlVVTEZ0N2Z3QWhYRHkzb05GVEF6RjJvOFB3",
#     "showActionMenu": False,
#     "shortViewCountText": {
#         "accessibility": {"accessibilityData": {"label": "36K views"}},
#         "simpleText": "36K views",
#     },
#     "menu": {
#         "menuRenderer": {
#             "items": [
#                 {
#                     "menuServiceItemRenderer": {
#                         "text": {"runs": [{"text": "Add to queue"}]},
#                         "icon": {"iconType": "ADD_TO_QUEUE_TAIL"},
#                         "serviceEndpoint": {
#                             "clickTrackingParams": "CNABEP6YBBgHIhMI0KHxvvjI_gIVaAtPCB0mcAuD",
#                             "commandMetadata": {
#                                 "webCommandMetadata": {"sendPost": True}
#                             },
#                             "signalServiceEndpoint": {
#                                 "signal": "CLIENT_SIGNAL",
#                                 "actions": [
#                                     {
#                                         "clickTrackingParams": "CNABEP6YBBgHIhMI0KHxvvjI_gIVaAtPCB0mcAuD",
#                                         "addToPlaylistCommand": {
#                                             "openMiniplayer": True,
#                                             "videoId": "CCGsMTzUkWM",
#                                             "listType": "PLAYLIST_EDIT_LIST_TYPE_QUEUE",
#                                             "onCreateListCommand": {
#                                                 "clickTrackingParams": "CNABEP6YBBgHIhMI0KHxvvjI_gIVaAtPCB0mcAuD",
#                                                 "commandMetadata": {
#                                                     "webCommandMetadata": {
#                                                         "sendPost": True,
#                                                         "apiUrl": "/youtubei/v1/playlist/create",
#                                                     }
#                                                 },
#                                                 "createPlaylistServiceEndpoint": {
#                                                     "videoIds": ["CCGsMTzUkWM"],
#                                                     "params": "CAQ%3D",
#                                                 },
#                                             },
#                                             "videoIds": ["CCGsMTzUkWM"],
#                                         },
#                                     }
#                                 ],
#                             },
#                         },
#                         "trackingParams": "CNABEP6YBBgHIhMI0KHxvvjI_gIVaAtPCB0mcAuD",
#                     }
#                 },
#                 {
#                     "menuServiceItemRenderer": {
#                         "text": {"runs": [{"text": "Share"}]},
#                         "icon": {"iconType": "SHARE"},
#                         "serviceEndpoint": {
#                             "clickTrackingParams": "CMwBENwwIhMI0KHxvvjI_gIVaAtPCB0mcAuD",
#                             "commandMetadata": {
#                                 "webCommandMetadata": {
#                                     "sendPost": True,
#                                     "apiUrl": "/youtubei/v1/share/get_share_panel",
#                                 }
#                             },
#                             "shareEntityServiceEndpoint": {
#                                 "serializedShareEntity": "CgtDQ0dzTVR6VWtXTQ%3D%3D",
#                                 "commands": [
#                                     {
#                                         "clickTrackingParams": "CMwBENwwIhMI0KHxvvjI_gIVaAtPCB0mcAuD",
#                                         "openPopupAction": {
#                                             "popup": {
#                                                 "unifiedSharePanelRenderer": {
#                                                     "trackingParams": "CM8BEI5iIhMI0KHxvvjI_gIVaAtPCB0mcAuD",
#                                                     "showLoadingSpinner": True,
#                                                 }
#                                             },
#                                             "popupType": "DIALOG",
#                                             "beReused": True,
#                                         },
#                                     }
#                                 ],
#                             },
#                         },
#                         "trackingParams": "CMwBENwwIhMI0KHxvvjI_gIVaAtPCB0mcAuD",
#                     }
#                 },
#             ],
#             "trackingParams": "CMwBENwwIhMI0KHxvvjI_gIVaAtPCB0mcAuD",
#             "accessibility": {"accessibilityData": {"label": "Action menu"}},
#         }
#     },
#     "thumbnailOverlays": [
#         {
#             "thumbnailOverlayTimeStatusRenderer": {
#                 "text": {
#                     "accessibility": {
#                         "accessibilityData": {"label": "5 minutes, 44 seconds"}
#                     },
#                     "simpleText": "5:44",
#                 },
#                 "style": "DEFAULT",
#             }
#         },
#         {
#             "thumbnailOverlayToggleButtonRenderer": {
#                 "isToggled": False,
#                 "untoggledIcon": {"iconType": "WATCH_LATER"},
#                 "toggledIcon": {"iconType": "CHECK"},
#                 "untoggledTooltip": "Watch later",
#                 "toggledTooltip": "Added",
#                 "untoggledServiceEndpoint": {
#                     "clickTrackingParams": "CM4BEPnnAxgCIhMI0KHxvvjI_gIVaAtPCB0mcAuD",
#                     "commandMetadata": {
#                         "webCommandMetadata": {
#                             "sendPost": True,
#                             "apiUrl": "/youtubei/v1/browse/edit_playlist",
#                         }
#                     },
#                     "playlistEditEndpoint": {
#                         "playlistId": "WL",
#                         "actions": [
#                             {
#                                 "addedVideoId": "CCGsMTzUkWM",
#                                 "action": "ACTION_ADD_VIDEO",
#                             }
#                         ],
#                     },
#                 },
#                 "toggledServiceEndpoint": {
#                     "clickTrackingParams": "CM4BEPnnAxgCIhMI0KHxvvjI_gIVaAtPCB0mcAuD",
#                     "commandMetadata": {
#                         "webCommandMetadata": {
#                             "sendPost": True,
#                             "apiUrl": "/youtubei/v1/browse/edit_playlist",
#                         }
#                     },
#                     "playlistEditEndpoint": {
#                         "playlistId": "WL",
#                         "actions": [
#                             {
#                                 "action": "ACTION_REMOVE_VIDEO_BY_VIDEO_ID",
#                                 "removedVideoId": "CCGsMTzUkWM",
#                             }
#                         ],
#                     },
#                 },
#                 "untoggledAccessibility": {
#                     "accessibilityData": {"label": "Watch later"}
#                 },
#                 "toggledAccessibility": {"accessibilityData": {"label": "Added"}},
#                 "trackingParams": "CM4BEPnnAxgCIhMI0KHxvvjI_gIVaAtPCB0mcAuD",
#             }
#         },
#         {
#             "thumbnailOverlayToggleButtonRenderer": {
#                 "untoggledIcon": {"iconType": "ADD_TO_QUEUE_TAIL"},
#                 "toggledIcon": {"iconType": "PLAYLIST_ADD_CHECK"},
#                 "untoggledTooltip": "Add to queue",
#                 "toggledTooltip": "Added",
#                 "untoggledServiceEndpoint": {
#                     "clickTrackingParams": "CM0BEMfsBBgDIhMI0KHxvvjI_gIVaAtPCB0mcAuD",
#                     "commandMetadata": {"webCommandMetadata": {"sendPost": True}},
#                     "signalServiceEndpoint": {
#                         "signal": "CLIENT_SIGNAL",
#                         "actions": [
#                             {
#                                 "clickTrackingParams": "CM0BEMfsBBgDIhMI0KHxvvjI_gIVaAtPCB0mcAuD",
#                                 "addToPlaylistCommand": {
#                                     "openMiniplayer": True,
#                                     "videoId": "CCGsMTzUkWM",
#                                     "listType": "PLAYLIST_EDIT_LIST_TYPE_QUEUE",
#                                     "onCreateListCommand": {
#                                         "clickTrackingParams": "CM0BEMfsBBgDIhMI0KHxvvjI_gIVaAtPCB0mcAuD",
#                                         "commandMetadata": {
#                                             "webCommandMetadata": {
#                                                 "sendPost": True,
#                                                 "apiUrl": "/youtubei/v1/playlist/create",
#                                             }
#                                         },
#                                         "createPlaylistServiceEndpoint": {
#                                             "videoIds": ["CCGsMTzUkWM"],
#                                             "params": "CAQ%3D",
#                                         },
#                                     },
#                                     "videoIds": ["CCGsMTzUkWM"],
#                                 },
#                             }
#                         ],
#                     },
#                 },
#                 "untoggledAccessibility": {
#                     "accessibilityData": {"label": "Add to queue"}
#                 },
#                 "toggledAccessibility": {"accessibilityData": {"label": "Added"}},
#                 "trackingParams": "CM0BEMfsBBgDIhMI0KHxvvjI_gIVaAtPCB0mcAuD",
#             }
#         },
#         {
#             "thumbnailOverlayNowPlayingRenderer": {
#                 "text": {"runs": [{"text": "Now playing"}]}
#             }
#         },
#     ],
#     "richThumbnail": {
#         "movingThumbnailRenderer": {
#             "movingThumbnailDetails": {
#                 "thumbnails": [
#                     {
#                         "url": "https://i.ytimg.com/an_webp/CCGsMTzUkWM/mqdefault_6s.webp?du=3000&sqp=CMX8pqIG&rs=AOn4CLCKTH6Qjh4BQwiaqq7mq3y_SzblUA",
#                         "width": 320,
#                         "height": 180,
#                     }
#                 ],
#                 "logAsMovingThumbnail": True,
#             },
#             "enableHoveredLogging": True,
#             "enableOverlay": True,
#         }
#     },
# }
