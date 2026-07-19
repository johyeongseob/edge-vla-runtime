from pathlib import Path

import imageio.v3 as iio
import mujoco


def main() -> None:
    xml = """
    <mujoco>
      <option timestep="0.004"/>
      <visual>
        <global offwidth="640" offheight="360"/>
      </visual>
      <asset>
        <texture name="grid" type="2d" builtin="checker" width="512" height="512"
                 rgb1="0.8 0.82 0.84" rgb2="0.55 0.58 0.62"/>
        <material name="floor" texture="grid" texrepeat="8 8" reflectance="0.1"/>
        <material name="box_mat" rgba="0.1 0.45 0.9 1"/>
      </asset>
      <worldbody>
        <light pos="0 -3 4" dir="0 1 -1"/>
        <geom name="floor" type="plane" size="2 2 0.05" material="floor"/>
        <body name="box" pos="-0.65 0 0.12">
          <joint name="slide_x" type="slide" axis="1 0 0"/>
          <geom type="box" size="0.12 0.12 0.12" material="box_mat"/>
        </body>
        <camera name="overview" pos="1.8 -2.2 1.35" xyaxes="0.78 0.63 0 -0.25 0.31 0.92"/>
      </worldbody>
    </mujoco>
    """

    model = mujoco.MjModel.from_xml_string(xml)
    data = mujoco.MjData(model)
    renderer = mujoco.Renderer(model, height=360, width=640)

    frames = []
    for step in range(300):
        target_x = 0.65
        error = target_x - data.qpos[0]
        data.ctrl[:] = 0
        data.qfrc_applied[0] = 6.0 * error - 1.5 * data.qvel[0]
        mujoco.mj_step(model, data)

        if step % 4 == 0:
            renderer.update_scene(data, camera="overview")
            frames.append(renderer.render())

    output_dir = Path("results")
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / "mujoco_motion.gif"
    iio.imwrite(output_path, frames, duration=50, loop=0)

    print(f"Saved MuJoCo motion: {output_path}")
    print(f"final box x: {data.qpos[0]:.6f}")


if __name__ == "__main__":
    main()
