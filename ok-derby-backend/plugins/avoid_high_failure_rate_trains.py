import auto_derby
from auto_derby import single_mode
from auto_derby import mathtools

class Training(single_mode.Training):
    def score(self, ctx: single_mode.Context) -> float:
        success_rate = mathtools.interpolate(
            int(ctx.vitality * 10000),
            (
                (0, 0.15),
                (1500, 0.3),
                (4000, 1.0),
            )
            if self.wisdom > 0
            else (
                (0, 0.01),
                (1500, 0.2),
                (3000, 0.5),
                (5000, 0.85),
                (7000, 1.0),
            ),
        )
        if success_rate < 0.7:
            return 0
        else:
            return super().score(ctx)


class Plugin(auto_derby.Plugin):
    def install(self) -> None:
        auto_derby.config.single_mode_training_class = Training


auto_derby.plugin.register(__name__, Plugin())
