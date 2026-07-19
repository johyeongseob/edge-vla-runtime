import mujoco


def main() -> None:
    xml = """
    <mujoco>
      <worldbody>
        <body name="box" pos="0 0 1">
          <joint type="free"/>
          <geom type="box" size="0.1 0.1 0.1"/>
        </body>
      </worldbody>
    </mujoco>
    """

    model = mujoco.MjModel.from_xml_string(xml)
    data = mujoco.MjData(model)

    initial_height = data.qpos[2]
    for _ in range(100):
        mujoco.mj_step(model, data)

    print("MuJoCo simulation OK")
    print(f"initial box height: {initial_height:.6f}")
    print(f"final box height: {data.qpos[2]:.6f}")


if __name__ == "__main__":
    main()
