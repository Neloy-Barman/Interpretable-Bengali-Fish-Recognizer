---
title: Recognizer
layout: page 
---


<!-- <iframe
	src="https://nelbarman053-bengali-fish-recognizer.hf.space"
	frameborder="0"
	width="850"
	height="450"
></iframe> -->

<!-- <script
	type="module"
	src="https://gradio.s3-us-west-2.amazonaws.com/4.8.0/gradio.js"
></script>

<gradio-app src="https://nelbarman053-bengali-fish-recognizer.hf.space"></gradio-app> -->


<input id="photo" type="file">

<div id="results"></div>


<script type="module">

	import { client } from "https://cdn.jsdelivr.net/npm/@gradio/client@0.1.4/dist/index.min.js";

    async function loaded(reader) {   
		const app = await client("https://nelbarman053-bengali-fish-recognizer.hf.space/--replicas/bgdp8/");
		
		const result = await app.predict("/predict", [
						reader.result, 	// blob in 'image_path' Image component
			]);

		// var label = result.data[0]['label']

		console.log(result);

		var image = result.data[0]

		var label = result.data[1]['label']

		// console.log("This is the explainable AI image: "+image)

		// console.log("This is the predicted category: "+label)

		results.innerHTML = 
		`
			<div style="display:grid;">
				<div>
					<h3>Original Image</h3>
					<img src = "${reader.result}" width="224" height="224">
				</div>
				<div>
					<h3>Explainable AI visualization</h3>
					<img src = "${image}" width="500" height="224">
				</div>
			</div>
			// <br/> <img src = "${image}" width="500"> <p>${label}</p>
		`;
    }


    function read() {
        const reader = new FileReader();
        reader.addEventListener('load', () => loaded(reader))
        reader.readAsDataURL(photo.files[0]);
    }

    photo.addEventListener('input', read);

</script>

