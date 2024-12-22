# *-* config: utf8 *-*

from src.scenes import scene as scene
import src.scene_manager as scene_manager


class Scene(scene.MenuScene):
    name = 'sceneloader'
    title = "Charger une scène"

    def __init__(self, name, config):
        super().__init__(name, {
            "select-sound": "menuSelect",
            "validate-sound": "menuValidate",
            "cancel-sound": "menuCancel",
            "choices": []
        })

    def activate(self, silent, params=None):
        idx = 0
        self.choices = []
        self.links = {}
        for name in scene_manager._INSTANCE._scenes:
            self.links[str(idx)] = name
            self.choices.append(name)
            idx += 1
        super().activate(silent, params)
