import re
a ={
    "result_num": 1,
    "result": [
        {
            "location": {
                "left": 117,
                "top": 131,
                "width": 172,
                "height": 170
            },
            "face_probability": 1,
            "rotation_angle": 2,
            "yaw": -0.34859421849251,
            "pitch": 2.3033397197723,
            "roll": 1.9135693311691,
            "landmark": [
                {
                    "x": 161.74819946289,
                    "y": 163.30244445801
                },
            ],
            "landmark72": [
                {
                    "x": 115.86531066895,
                    "y": 170.0546875
                },
            ],
            "age": 29.298097610474,
            "beauty": 55.128883361816,
            "expression": 1,
            "expression_probablity": 0.5543018579483,
            "gender": "male",
            "gender_probability": 0.99979132413864,
            "glasses": 0,
            "glasses_probability": 0.99999964237213,
            "race": "yellow",
            "race_probability": 0.99999976158142,
            "qualities": {
                "occlusion": {
                    "left_eye": 0,
                    "right_eye": 0,
                    "nose": 0,
                    "mouth": 0,
                    "left_cheek": 0.0064102564938366,
                    "right_cheek": 0.0057411273010075,
                    "chin": 0
                },
                "blur": 1.1886881756684e-10,
                "illumination": 141,
                "completeness": 1,
                "type": {
                    "human": 0.99935841560364,
                    "cartoon": 0.00064159056637436
                }
            }
        }
    ],
    "log_id": 2493878179101621
}

print(type(a))
# print(a.get("result"))
b = a.get("result")
print(b)
print(type(b))
c = str(b)
d= c.split(":")
for i in range(30):
    print(i)
    print(d[i])
