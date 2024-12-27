from src.scenes.TrainStation import *

def test_train_station_scene_init():
    config = {
        "type": "trainstation",
        "name": "Gare de test",
        "length": 600.0,
        "width": 50.0,
        "content": [
            {"type": "line",
             "name": "A",
             "width": 8.0,
             "length": 200.0
             },
            {"type": "platform",
             "width": 12.0,
             "length": 450.0
             },
            {"type": "line",
             "name": "B",
             "width": 8.0,
             "length": 400.0,
             },
            {"type": "line",
             "name": "C",
             "width": 8.0,
             "length": 300.0
             },
            {"type": "platform",
             "width": 12.0,
             "length": 450.0
             }
        ]
    }

    scene = Scene(config["name"], config)
    assert len(scene._content) == 5
