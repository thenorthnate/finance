# Configuration, variables, settings, etc
# Nathan North

class ApplicationSettings:
    mainMenu = {}
    mainWindow = {
        "metaData":{
            "title":"Finance Tool"
        },
        "geometry":{
            "width":500,
            "height":500,
            "xOffset":400,
            "yOffset":100
        },
        "frames":{
            "self":{
                "location":{"row":0, "column":0}
            },
            "topFrame":{
                "location":{"row":0, "column":0},
                "widgets":{
                    "welcomeLabel":{
                        "location":{"row":0, "column":0},
                        "padding":{"padx":None, "pady":None, "ipadx":None, "ipady":None}
                    },
                    "searchEntry":{
                        "location":{"row":0, "column":1},
                        "padding":{"padx":400, "pady":None, "ipadx":None, "ipady":None}
                    }
                }
            },
            "middleFrame":{
                
            }
        }
    }
