import numpy as np
import openvino as ov


def main() -> None:
    opset = ov.opset13

    x = opset.parameter([1, 4], ov.Type.f32, name="x")
    weight = opset.constant(np.array([[1.0, -1.0, 0.5, 2.0]], dtype=np.float32))
    y = opset.relu(opset.add(x, weight))
    model = ov.Model([y], [x], "tiny_openvino_test")

    core = ov.Core()
    compiled_model = core.compile_model(model, "CPU")

    input_data = np.array([[1.0, 2.0, -1.0, 0.5]], dtype=np.float32)
    result = compiled_model(input_data)[0]

    print("OpenVINO CPU inference OK")
    print("input:", input_data.tolist())
    print("output:", result.tolist())


if __name__ == "__main__":
    main()
