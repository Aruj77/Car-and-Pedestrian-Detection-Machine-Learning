# Car-Detection-Machine-Learning
In this project the code is using harcascade model of machine learning to detect cars and pedestrian.

For Example-

![car_image](https://user-images.githubusercontent.com/68498812/202897468-447c12c7-e4ab-4bfe-b5cf-4837a3702222.jpg)

Here all the cars will be detected.

# What are Haar Cascades?
Haar cascade is an algorithm that can detect objects in images, irrespective of their scale in image and location.

This algorithm is not so complex and can run in real-time. We can train a haar-cascade detector to detect various objects like cars, bikes, buildings, fruits, etc.

Haar cascade uses the cascading window, and it tries to compute features in every window and classify whether it could be an object. For more details on its working, refer to this <a href="https://medium.com/analytics-vidhya/haar-cascades-explained-38210e57970d">link</a>.

![image](https://user-images.githubusercontent.com/68498812/202897565-6c5641c0-f0f5-42fc-b57c-b11084f55f75.png)
Sample haar features traverse in window-sized across the picture to compute and match features.

Haar cascade works as a classifier. It classifies positive data points → that are part of our detected object and negative data points → that don’t contain our object.
<ul>
<li>Haar cascades are fast and can work well in real-time.</li>
<li>Haar cascade is not as accurate as modern object detection techniques are.</li>
<li>Haar cascade has a downside. It predicts many false positives.</li>
<li>Simple to implement, less computing power required.</li>
</ul>
