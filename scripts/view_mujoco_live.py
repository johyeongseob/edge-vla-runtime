import time

import mujoco
import mujoco.viewer


def main() -> None:
    xml = """
    <mujoco>
      <option timestep="0.004"/>
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
      </worldbody>
    </mujoco>
    """

    model = mujoco.MjModel.from_xml_string(xml)
    data = mujoco.MjData(model)
    target_x = 0.65

    with mujoco.viewer.launch_passive(model, data) as viewer:
        viewer.cam.distance = 2.4
        viewer.cam.azimuth = 135
        viewer.cam.elevation = -25
        viewer.cam.lookat[:] = [0.0, 0.0, 0.2]

        while viewer.is_running():
            step_start = time.time()

            error = target_x - data.qpos[0]
            data.qfrc_applied[0] = 6.0 * error - 1.5 * data.qvel[0]
            mujoco.mj_step(model, data)

            viewer.sync()

            elapsed = time.time() - step_start
            if elapsed < model.opt.timestep:
                time.sleep(model.opt.timestep - elapsed)


if __name__ == "__main__":
    main()
