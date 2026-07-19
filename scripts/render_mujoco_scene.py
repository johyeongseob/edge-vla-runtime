from pathlib import Path

import mujoco


def main() -> None:
    xml = """
    <mujoco>
      <visual>
        <global offwidth="960" offheight="540"/>
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
        <body name="box" pos="0 0 1">
          <joint type="free"/>
          <geom type="box" size="0.12 0.12 0.12" material="box_mat"/>
        </body>
        <camera name="overview" pos="1.8 -2.2 1.4" xyaxes="0.78 0.63 0 -0.25 0.31 0.92"/>
      </worldbody>
    </mujoco>
    """

    model = mujoco.MjModel.from_xml_string(xml)
    data = mujoco.MjData(model)

    for _ in range(180):
        mujoco.mj_step(model, data)

    renderer = mujoco.Renderer(model, height=540, width=960)
    renderer.update_scene(data, camera="overview")
    pixels = renderer.render()

    output_dir = Path("results")
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / "mujoco_scene.png"

    import imageio.v3 as iio

    iio.imwrite(output_path, pixels)
    print(f"Saved MuJoCo render: {output_path}")
    print(f"final box height: {data.qpos[2]:.6f}")


if __name__ == "__main__":
    main()
