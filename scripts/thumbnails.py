import scrapetube
import requests

videos = scrapetube.get_channel(channel_url="https://www.youtube.com/c/theneedledrop")
videos = (v for v in videos if v["title"]["runs"][0]["text"].endswith("ALBUM REVIEW"))

for v in videos:
    id = v["videoId"]
    tn = v["thumbnail"]["thumbnails"][0]["url"]
    r = requests.get(tn)
    with open(f"thumbnails/{id}.jpg", "wb") as f:
        f.write(r.content)
# for video in videos:
#     print(video["videoId"])

# #%%
# from pytube import Channel
# import requests as req


# url = "https://www.youtube.com/c/theneedledrop"
# c = Channel(url)

# #%%
# videos = (v for v in c.videos_generator() if v.title.endswith("ALBUM REVIEW"))

# for v in videos:
#     tn = v.thumbnail_url
#     r = req.get(tn)
#     with open(f"{v.title}.jpg", "wb") as f:
#         f.write(r.content)

# {
#   "videoId": "CCGsMTzUkWM",
#   "thumbnail": {
#     "thumbnails": [
#       {
#         "url": "https://i.ytimg.com/vi/CCGsMTzUkWM/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLClfIGW_FrvYGc6Ae3G0NmoXC3GHQ",
#         "width": 168,
#         "height": 94
#       },
#       {
#         "url": "https://i.ytimg.com/vi/CCGsMTzUkWM/hqdefault.jpg?sqp=-oaymwEbCMQBEG5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLCR3LBdbi0Jb9JimfqmBl7zRXNeMw",
#         "width": 196,
#         "height": 110
#       },
#       {
#         "url": "https://i.ytimg.com/vi/CCGsMTzUkWM/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLASCeELZBwuQPff_ticRfezAIN-_A",
#         "width": 246,
#         "height": 138
#       },
#       {
#         "url": "https://i.ytimg.com/vi/CCGsMTzUkWM/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLA1Tgze64K6td3IUA-OnUz6toXsgw",
#         "width": 336,
#         "height": 188
#       }
#     ]
#   },
#   "title": {
#     "runs": [
#       {
#         "text": "HMLTD - The Worm ALBUM REVIEW"
#       }
#     ],
#     "accessibility": {
#       "accessibilityData": {
#         "label": "HMLTD - The Worm ALBUM REVIEW by theneedledrop 16 hours ago 5 minutes, 44 seconds 33,249 views"
#       }
#     }
#   },
#   "descriptionSnippet": {
#     "runs": [
#       {
#         "text": "Listen: https://hmltd.bandcamp.com/album/the-worm\n\nThe songwriting and performances on The Worm are kind of an iffy foundation for HMLTD's conceptual and stylistic ambitions.\n\nMore rock reviews:..."
#       }
#     ]
#   },
#   "publishedTimeText": {
#     "simpleText": "16 hours ago"
#   },
#   "lengthText": {
#     "accessibility": {
#       "accessibilityData": {
#         "label": "5 minutes, 44 seconds"
#       }
#     },
#     "simpleText": "5:44"
#   },
#   "viewCountText": {
#     "simpleText": "33,249 views"
#   },
#   "navigationEndpoint": {
#     "clickTrackingParams": "COkBENwwIhMIqOWElr_I_gIVRApPCB0dAQNkWhhVQ3Q3ZndBaFhEeTNvTkZUQXpGMm84UHeaAQYQ8jgY4AeqARpVVUxGdDdmd0FoWER5M29ORlRBekYybzhQdw==",
#     "commandMetadata": {
#       "webCommandMetadata": {
#         "url": "/watch?v=CCGsMTzUkWM",
#         "webPageType": "WEB_PAGE_TYPE_WATCH",
#         "rootVe": 3832
#       }
#     },
#     "watchEndpoint": {
#       "videoId": "CCGsMTzUkWM",
#       "watchEndpointSupportedOnesieConfig": {
#         "html5PlaybackOnesieConfig": {
#           "commonConfig": {
#             "url": "https://rr2---sn-5uaeznlz.googlevideo.com/initplayback?source=youtube&oeis=1&c=WEB&oad=3200&ovd=3200&oaad=11000&oavd=11000&ocs=700&oewis=1&oputc=1&ofpcc=1&msp=1&odepv=1&id=0821ac313cd49163&ip=98.251.104.56&initcwndbps=1748750&mt=1682544289&oweuc="
#           }
#         }
#       }
#     }
#   },
#   "ownerBadges": [
#     {
#       "metadataBadgeRenderer": {
#         "icon": {
#           "iconType": "CHECK_CIRCLE_THICK"
#         },
#         "style": "BADGE_STYLE_TYPE_VERIFIED",
#         "tooltip": "Verified",
#         "trackingParams": "COkBENwwIhMIqOWElr_I_gIVRApPCB0dAQNk",
#         "accessibilityData": {
#           "label": "Verified"
#         }
#       }
#     }
#   ],
#   "trackingParams": "COkBENwwIhMIqOWElr_I_gIVRApPCB0dAQNkQOOi0uaThuuQCKoBGlVVTEZ0N2Z3QWhYRHkzb05GVEF6RjJvOFB3",
#   "showActionMenu": false,
#   "shortViewCountText": {
#     "accessibility": {
#       "accessibilityData": {
#         "label": "33K views"
#       }
#     },
#     "simpleText": "33K views"
#   },
#   "menu": {
#     "menuRenderer": {
#       "items": [
#         {
#           "menuServiceItemRenderer": {
#             "text": {
#               "runs": [
#                 {
#                   "text": "Add to queue"
#                 }
#               ]
#             },
#             "icon": {
#               "iconType": "ADD_TO_QUEUE_TAIL"
#             },
#             "serviceEndpoint": {
#               "clickTrackingParams": "CO4BEP6YBBgHIhMIqOWElr_I_gIVRApPCB0dAQNk",
#               "commandMetadata": {
#                 "webCommandMetadata": {
#                   "sendPost": true
#                 }
#               },
#               "signalServiceEndpoint": {
#                 "signal": "CLIENT_SIGNAL",
#                 "actions": [
#                   {
#                     "clickTrackingParams": "CO4BEP6YBBgHIhMIqOWElr_I_gIVRApPCB0dAQNk",
#                     "addToPlaylistCommand": {
#                       "openMiniplayer": true,
#                       "videoId": "CCGsMTzUkWM",
#                       "listType": "PLAYLIST_EDIT_LIST_TYPE_QUEUE",
#                       "onCreateListCommand": {
#                         "clickTrackingParams": "CO4BEP6YBBgHIhMIqOWElr_I_gIVRApPCB0dAQNk",
#                         "commandMetadata": {
#                           "webCommandMetadata": {
#                             "sendPost": true,
#                             "apiUrl": "/youtubei/v1/playlist/create"
#                           }
#                         },
#                         "createPlaylistServiceEndpoint": {
#                           "videoIds": [
#                             "CCGsMTzUkWM"
#                           ],
#                           "params": "CAQ%3D"
#                         }
#                       },
#                       "videoIds": [
#                         "CCGsMTzUkWM"
#                       ]
#                     }
#                   }
#                 ]
#               }
#             },
#             "trackingParams": "CO4BEP6YBBgHIhMIqOWElr_I_gIVRApPCB0dAQNk"
#           }
#         },
#         {
#           "menuServiceItemDownloadRenderer": {
#             "serviceEndpoint": {
#               "clickTrackingParams": "CO0BENGqBRgIIhMIqOWElr_I_gIVRApPCB0dAQNk",
#               "offlineVideoEndpoint": {
#                 "videoId": "CCGsMTzUkWM",
#                 "onAddCommand": {
#                   "clickTrackingParams": "CO0BENGqBRgIIhMIqOWElr_I_gIVRApPCB0dAQNk",
#                   "getDownloadActionCommand": {
#                     "videoId": "CCGsMTzUkWM",
#                     "params": "CAI%3D"
#                   }
#                 }
#               }
#             },
#             "trackingParams": "CO0BENGqBRgIIhMIqOWElr_I_gIVRApPCB0dAQNk"
#           }
#         },
#         {
#           "menuServiceItemRenderer": {
#             "text": {
#               "runs": [
#                 {
#                   "text": "Share"
#                 }
#               ]
#             },
#             "icon": {
#               "iconType": "SHARE"
#             },
#             "serviceEndpoint": {
#               "clickTrackingParams": "COkBENwwIhMIqOWElr_I_gIVRApPCB0dAQNk",
#               "commandMetadata": {
#                 "webCommandMetadata": {
#                   "sendPost": true,
#                   "apiUrl": "/youtubei/v1/share/get_share_panel"
#                 }
#               },
#               "shareEntityServiceEndpoint": {
#                 "serializedShareEntity": "CgtDQ0dzTVR6VWtXTQ%3D%3D",
#                 "commands": [
#                   {
#                     "clickTrackingParams": "COkBENwwIhMIqOWElr_I_gIVRApPCB0dAQNk",
#                     "openPopupAction": {
#                       "popup": {
#                         "unifiedSharePanelRenderer": {
#                           "trackingParams": "COwBEI5iIhMIqOWElr_I_gIVRApPCB0dAQNk",
#                           "showLoadingSpinner": true
#                         }
#                       },
#                       "popupType": "DIALOG",
#                       "beReused": true
#                     }
#                   }
#                 ]
#               }
#             },
#             "trackingParams": "COkBENwwIhMIqOWElr_I_gIVRApPCB0dAQNk"
#           }
#         }
#       ],
#       "trackingParams": "COkBENwwIhMIqOWElr_I_gIVRApPCB0dAQNk",
#       "accessibility": {
#         "accessibilityData": {
#           "label": "Action menu"
#         }
#       }
#     }
#   },
#   "thumbnailOverlays": [
#     {
#       "thumbnailOverlayTimeStatusRenderer": {
#         "text": {
#           "accessibility": {
#             "accessibilityData": {
#               "label": "5 minutes, 44 seconds"
#             }
#           },
#           "simpleText": "5:44"
#         },
#         "style": "DEFAULT"
#       }
#     },
#     {
#       "thumbnailOverlayToggleButtonRenderer": {
#         "isToggled": false,
#         "untoggledIcon": {
#           "iconType": "WATCH_LATER"
#         },
#         "toggledIcon": {
#           "iconType": "CHECK"
#         },
#         "untoggledTooltip": "Watch later",
#         "toggledTooltip": "Added",
#         "untoggledServiceEndpoint": {
#           "clickTrackingParams": "COsBEPnnAxgCIhMIqOWElr_I_gIVRApPCB0dAQNk",
#           "commandMetadata": {
#             "webCommandMetadata": {
#               "sendPost": true,
#               "apiUrl": "/youtubei/v1/browse/edit_playlist"
#             }
#           },
#           "playlistEditEndpoint": {
#             "playlistId": "WL",
#             "actions": [
#               {
#                 "addedVideoId": "CCGsMTzUkWM",
#                 "action": "ACTION_ADD_VIDEO"
#               }
#             ]
#           }
#         },
#         "toggledServiceEndpoint": {
#           "clickTrackingParams": "COsBEPnnAxgCIhMIqOWElr_I_gIVRApPCB0dAQNk",
#           "commandMetadata": {
#             "webCommandMetadata": {
#               "sendPost": true,
#               "apiUrl": "/youtubei/v1/browse/edit_playlist"
#             }
#           },
#           "playlistEditEndpoint": {
#             "playlistId": "WL",
#             "actions": [
#               {
#                 "action": "ACTION_REMOVE_VIDEO_BY_VIDEO_ID",
#                 "removedVideoId": "CCGsMTzUkWM"
#               }
#             ]
#           }
#         },
#         "untoggledAccessibility": {
#           "accessibilityData": {
#             "label": "Watch later"
#           }
#         },
#         "toggledAccessibility": {
#           "accessibilityData": {
#             "label": "Added"
#           }
#         },
#         "trackingParams": "COsBEPnnAxgCIhMIqOWElr_I_gIVRApPCB0dAQNk"
#       }
#     },
#     {
#       "thumbnailOverlayToggleButtonRenderer": {
#         "untoggledIcon": {
#           "iconType": "ADD_TO_QUEUE_TAIL"
#         },
#         "toggledIcon": {
#           "iconType": "PLAYLIST_ADD_CHECK"
#         },
#         "untoggledTooltip": "Add to queue",
#         "toggledTooltip": "Added",
#         "untoggledServiceEndpoint": {
#           "clickTrackingParams": "COoBEMfsBBgDIhMIqOWElr_I_gIVRApPCB0dAQNk",
#           "commandMetadata": {
#             "webCommandMetadata": {
#               "sendPost": true
#             }
#           },
#           "signalServiceEndpoint": {
#             "signal": "CLIENT_SIGNAL",
#             "actions": [
#               {
#                 "clickTrackingParams": "COoBEMfsBBgDIhMIqOWElr_I_gIVRApPCB0dAQNk",
#                 "addToPlaylistCommand": {
#                   "openMiniplayer": true,
#                   "videoId": "CCGsMTzUkWM",
#                   "listType": "PLAYLIST_EDIT_LIST_TYPE_QUEUE",
#                   "onCreateListCommand": {
#                     "clickTrackingParams": "COoBEMfsBBgDIhMIqOWElr_I_gIVRApPCB0dAQNk",
#                     "commandMetadata": {
#                       "webCommandMetadata": {
#                         "sendPost": true,
#                         "apiUrl": "/youtubei/v1/playlist/create"
#                       }
#                     },
#                     "createPlaylistServiceEndpoint": {
#                       "videoIds": [
#                         "CCGsMTzUkWM"
#                       ],
#                       "params": "CAQ%3D"
#                     }
#                   },
#                   "videoIds": [
#                     "CCGsMTzUkWM"
#                   ]
#                 }
#               }
#             ]
#           }
#         },
#         "untoggledAccessibility": {
#           "accessibilityData": {
#             "label": "Add to queue"
#           }
#         },
#         "toggledAccessibility": {
#           "accessibilityData": {
#             "label": "Added"
#           }
#         },
#         "trackingParams": "COoBEMfsBBgDIhMIqOWElr_I_gIVRApPCB0dAQNk"
#       }
#     },
#     {
#       "thumbnailOverlayNowPlayingRenderer": {
#         "text": {
#           "runs": [
#             {
#               "text": "Now playing"
#             }
#           ]
#         }
#       }
#     }
#   ],
#   "richThumbnail": {
#     "movingThumbnailRenderer": {
#       "movingThumbnailDetails": {
#         "thumbnails": [
#           {
#             "url": "https://i.ytimg.com/an_webp/CCGsMTzUkWM/mqdefault_6s.webp?du=3000&sqp=CNKppqIG&rs=AOn4CLC4cZehI8z_4EGsqBcRqHQFb5rF5w",
#             "width": 320,
#             "height": 180
#           }
#         ],
#         "logAsMovingThumbnail": true
#       },
#       "enableHoveredLogging": true,
#       "enableOverlay": true
#     }
#   }
# }
