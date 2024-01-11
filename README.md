# Bengali-Fish-Recognizer

<h2>Project Development Journal</h2>

<h3><code style="color:blue">Problem Statement</code></h3>

<strong>A bengali fish image recognizer that can classify in between: -</strong>

<div align="center">
    <table>
        <tr>
            <td><img src="https://github.com/Neloy-Barman/Bengali-Fish-Recognizer/assets/110896263/5b53977e-8a36-4318-adb8-30d307a3aaf6" height="200" width="200"></td>
            <td><img src="https://github.com/Neloy-Barman/Bengali-Fish-Recognizer/assets/110896263/7a9918cf-3520-43b6-b897-ef0b839bc9b0" height="200" width="200"></td>
            <td><img src="https://github.com/Neloy-Barman/Bengali-Fish-Recognizer/assets/110896263/a8ba2dcb-c0d3-4b05-8cfb-8d26874fe91a" height="200" width="200"></td>
            <td><img src="https://github.com/Neloy-Barman/Bengali-Fish-Recognizer/assets/110896263/3a86184d-e038-46e1-96b8-f4dd3d7fe03b" height="200" width="200"></td>
        <tr>
        <tr>
            <th>Ayre</th>
            <th>Catla</th>
            <th>Chital</th>
            <th>Ilish</th>
        </tr>
        <tr>
            <td><img src="https://github.com/Neloy-Barman/Bengali-Fish-Recognizer/assets/110896263/bec208cc-ef5f-4701-a6bb-3c2b10ca9f0e" height="200" width="200"></td>
            <td><img src="https://github.com/Neloy-Barman/Bengali-Fish-Recognizer/assets/110896263/8ddd98a5-0707-41c9-8bf1-33557479bb27" height="200" width="200"></td>
            <td><img src="https://github.com/Neloy-Barman/Bengali-Fish-Recognizer/assets/110896263/4c97f6c5-1646-4dee-a482-5a987a49df67" height="200" width="200"></td>
            <td><img src="https://github.com/Neloy-Barman/Bengali-Fish-Recognizer/assets/110896263/aacb3a06-5d21-403d-8a9d-26e5af5e34cd" height="200" width="200"></td>
        <tr>
        <tr>
            <th>Kachki</th>
            <th>Kajoli</th>
            <th>Koi</th>
            <th>Magur</th>
        </tr>
        <tr>
            <td><img src="https://github.com/Neloy-Barman/Bengali-Fish-Recognizer/assets/110896263/e52f453a-1507-4bb2-bb4e-3b24adb6bde5" height="200" width="200"></td>
            <td><img src="https://github.com/Neloy-Barman/Bengali-Fish-Recognizer/assets/110896263/d34bec60-d838-4bc3-a1f7-144fcd6490a2" height="200" width="200"></td>
            <td><img src="https://github.com/Neloy-Barman/Bengali-Fish-Recognizer/assets/110896263/cdf9daf4-7a44-4091-9e89-63081ab3e464" height="200" width="200"></td>
            <td><img src="https://github.com/Neloy-Barman/Bengali-Fish-Recognizer/assets/110896263/f03d97aa-d457-4231-80f5-7bec96098947" height="200" width="200"></td>
        <tr>
        <tr>
            <th>Mola Dhela</th>
            <th>Mrigal</th>
            <th>Pabda</th>
            <th>Pangash</th>
        </tr>
        <tr>
            <td><img src="https://github.com/Neloy-Barman/Bengali-Fish-Recognizer/assets/110896263/25cebc38-d4f1-4c2a-9388-e65841f110bf" height="200" width="200"></td>
            <td><img src="https://github.com/Neloy-Barman/Bengali-Fish-Recognizer/assets/110896263/5542b40c-52bc-4233-b6d2-2cb605dfb419" height="200" width="200"></td>
            <td><img src="https://github.com/Neloy-Barman/Bengali-Fish-Recognizer/assets/110896263/384f348e-d703-4466-8cc6-f3184967f498" height="200" width="200"></td>
            <td><img src="https://github.com/Neloy-Barman/Bengali-Fish-Recognizer/assets/110896263/e7aeda22-d95e-426c-82ea-9dcfce69125d" height="200" width="200"></td>
        <tr>
        <tr>
            <th>Poa</th>
            <th>Puti</th>
            <th>Rui</th>
            <th>Shing</th>
        </tr>
        <tr>
            <td><img src="https://github.com/Neloy-Barman/Bengali-Fish-Recognizer/assets/110896263/fe43bc2c-e3db-48bd-b2a4-63dec4175279" height="200" width="200"></td>
            <td><img src="https://github.com/Neloy-Barman/Bengali-Fish-Recognizer/assets/110896263/71b41ca6-1b94-4130-bbac-04c1321aa0e7" height="200" width="200"></td>
            <td><img src="https://github.com/Neloy-Barman/Bengali-Fish-Recognizer/assets/110896263/c17eb7dd-da1a-428f-acda-4f9841677311" height="200" width="200"></td>
            <td><img src="https://github.com/Neloy-Barman/Bengali-Fish-Recognizer/assets/110896263/92cd2449-0638-47c9-80b2-13825b03ed81" height="200" width="200"></td>
        <tr>
        <tr>
            <th>Silver Carp</th>
            <th>Taki</th>
            <th>Telapia</th>
            <th>Tengra</th>
        </tr>
    </table>
</div>

<h3><code style="color:blue">Objective</code></h3>
<strong>There are many kinds of fishes sold in Bangladeshi fish markets. Each of them has their own characteristics.But there are a few that sometimes look alike but can be differentiated using tiny details. Such as, A Catla fish's head size is larger than the Rui's but other features are almost same. Ayre and Pangash both have same body structure but an ayre fish has hackeles whereas pangash doesn't fall in catfish category. There are many fishes like that. The main goal of this recognizer project is to categorize in between them.</strong>

<h3><code style="color:blue">Data Collection</code></h3>
<strong>A bit of exploration made me know that searching a fish with its scientific name gives better result and provides with more accurate images. So, I mapped each fish's bengali and scientific name within a dictionary. Then using fastAI's <a href="https://duckduckgo.com/">DuckDuckGo</a> searching, running a loop within the dictionary, I collected images for each category and kept them in their respective folders. You will found the whole procedure within the "data_collection" notebook.</strong>

<h3><code style="color:blue">Data Cleaning</code></h3>
<strong>There were many redundant images within many categories. In some cases, images were mixed up between catgories. So, before training I not only had to delete those redundant images but also needed to move images to their respective folders. Still, as humen we sometimes fail to do each thing perfect.<br/>

<div align="center">
    <img src="readmeFileImages/redundant_image_1.png" height="200" width="850"><br/>
    <img src="readmeFileImages/redundant_image_2.png" height="200" width="850">
</div> 

After model training, when the results were not satisfactory, I found the classes with most losses and repeated the cleaning process. In the end, if you look at the images distribution table, you will find out that it turned out to be an imbalanced dataset.</strong>
<table align="center">
    <tr>
        <th align="center" colspan="2"><strong>Images Distribution</strong></th>
    </tr>
    <tr>
        <th align="center">Before Cleaning</th>
        <th align="center">After Cleaning</th>
    </tr>
    <tr>
        <td align="center"><img src="readmeFileImages/before.png" height="350" width="350"></td>
        <td align="center"><img src="readmeFileImages/after.png" height="350" width="350"></td>
    </tr>
</table>

<h3><code style="color:blue">Dataloader Preparation</code></h3>
<strong>I splitted the whole data to. I prepared the dataloader with a batch size of 32.</strong>

<h3><code style="color:blue">Models Experimentations</code></h3>
<strong>To create the classifier, I chose some pre-trained and well-performing computer vision models with feature extractors avaialable in the fastAI and trained them. I selected these models from my previous research-based experience. The choosen ones are: - 
    <ul>
      <li>VGG-19</li>
      <li>DenseNet-121</li>  
      <li>ResNet-50</li>  
    </ul>
</strong>

<h3><code style="color:blue">Performance Evaluation</code></h3>

<h3><code style="color:blue">Explainablity</code></h3>
<strong>To interpret the model's performances, I applied Grad-CAM, a gradient-based method. Within an image, we can find which region was found important by a model for the predicted class.</strong> 
<table align="center">
    <tr align="center">
        <th colspan="4">Correctly classified visualizations</th>
    </tr>
    <tr align="center">
        <th>Actual Image</th>
        <th>ResNet-50</th>
        <th>DenseNet-121</th>
        <th>VGG-19</th>
    </tr>
    <tr align="center">
        <td><img src="testData/unknown_01.jpg" height="200" width="200"></td>
        <td><img src="readmeFileImages/resnet50_correct.png" height="200" width="200"></td>
        <td><img src="readmeFileImages/densenet121_correct.png" height="200" width="200"></td>
        <td><img src="readmeFileImages/vgg19_correct.png" height="200" width="200"></td>
    </tr>
    <tr align="center">
        <td><p>Rui</p></td>
        <td><p>Rui</p></td>
        <td><p>Rui</p></td>
        <td><p>Rui</p></td>
    </tr>
       <tr align="center">
        <th colspan="4">Mis-classified visualizations</th>
    </tr>
    <tr align="center">
        <th>Actual Image</th>
        <th>ResNet-50</th>
        <th>DenseNet-121</th>
        <th>VGG-19</th>
    </tr>
    <tr align="center">
        <td><img src="testData/unknown_10.jpg" height="200" width="200"></td>
        <td><img src="readmeFileImages/resnet50_mis.png" height="200" width="200"></td>
        <td><img src="readmeFileImages/densenet121_mis.png" height="200" width="200"></td>
        <td><img src="readmeFileImages/vgg19_mis.png" height="200" width="200"></td>
    </tr>
    <tr align="center">
        <td><p>Koi</p></td>
        <td><p>Telapia</p></td>
        <td><p>Taki</p></td>
        <td><p>Telapia</p></td>
    </tr>
</table>
<strong>By looking at the Resnet-50's xai mask, we can say that it tries to find characteristics properly. For example, in the case of correctly classified image, it's locating regions nearby tail and head, even in the case of misclassification, it's marking more features within body area. But in the case of DenseNet-121, the masked areas are scattered more at outiside in both the cases. Vgg-19 while correctly classifying is locating the middle body area but more areas were masked than the required region. For the misclassification, it located within the image but stil missed the correct label.</strong>           

<h3><code style="color:blue">Deployment</code></h3>
<strong>As ResNet-50 was showing better performance than others. So,I deployed the recognizer using gradio app within Huggingface. Check out the <a href="https://huggingface.co/spaces/nelbarman053/Bengali-Fish-Recognizer">deployment</a> & <a href="https://huggingface.co/spaces/nelbarman053/Bengali-Fish-Recognizer/tree/main">required files</a> for the deployment.</strong> 
<div align="center">
    <img src="readmeFileImages/gradio_deployment.png" height="450" width="900">
</div>

<h3><code style="color:blue">Integration</code></h3>

<strong>The recognizer model is integrated using github pages and jekyll remote theme.<br/>
Check out the ingtegration of <a href="https://neloy-barman.github.io/Bengali-Fish-Recognizer/">Bengali Fish Recognizer</a></strong>
