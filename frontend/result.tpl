<!DOCTYPE HTML>
<!--
	Lens by HTML5 UP
	html5up.net | @n33co
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
	<head>
		<title>Car Searcher</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<!--[if lte IE 8]><script src="frontend/assets/js/ie/html5shiv.js"></script><![endif]-->
		<link rel="stylesheet" href="frontend/assets/css/main.css" />
		<link rel="shortcut icon" href="frontend/favicon.ico" type="image/x-icon" />
		<!--[if lte IE 8]><link rel="stylesheet" href="frontend/assets/css/ie8.css" /><![endif]-->
		<!--[if lte IE 9]><link rel="stylesheet" href="frontend/assets/css/ie9.css" /><![endif]-->
		<noscript><link rel="stylesheet" href="frontend/assets/css/noscript.css" /></noscript>
	</head>
	<body class="is-loading-0 is-loading-1 is-loading-2">

		<!-- Main -->
			<div id="main">

				<!-- Header -->
					<header id="header">										
						<h1>10 Best Match Results</h1>
                        <label>Estimated time execution: {{time_exec}} seconds.</label><hr>
						<ul class="icons">
							<li><a href="/" class="icon fa-home"><span class="label">Home</span></a></li>
							<li><a href="http://www.twitter.com/habibieeddien" class="icon fa-twitter"><span class="label">Twitter</span></a></li>
							<li><a href="http://www.itb.ac.id" class="icon fa-instagram"><span class="label">Instagram</span></a></li>
							<li><a href="http://github.com/habibieeddien" class="icon fa-github"><span class="label">Github</span></a></li>
							<li><a href="mailto:habibieeddien@students.itb.ac.id" class="icon fa-envelope-o"><span class="label">Email</span></a></li>
						</ul>
					</header>
<hr>
				<!-- Thumbnail -->
					<section id="thumbnails">
						<article>
							<a class="thumbnail" href="/queries/{{query}}" data-position="top center"><img src="/queries/{{query}}" alt="Your Query" /></a>
							<h2>Your Query Image</h2>
							<p style="background-color:#000;">This is your image.</p>
						</article>
					% for (score,image) in bestMatch:
						% id = int(image[:image.find("_")])
						% info = infocar[id]
						<article>
							<a class="thumbnail" href="/datacars/{{image}}" data-position="top center"><img src="/datacars/{{image}}" alt="{{info[0]}}" /></a>
							<h2>{{info[0]}}</h2>
							<p style="background-color:#000;">
								<b>Type:</b> {{info[1]}} | {{info[2]}} | {{info[3]}} | <b>Maker:</b> {{info[4]}} | <b>Country:</b> {{info[5]}}<br>
                                <i><h5>(Similarity Dist: {{score}})</h5></i>
							</p>
						</article>
					% end
						
					</section>
<hr>
				<!-- Footer -->
					<footer id="footer">
						<ul class="copyright">
							<li>&copy; Car Searcher.</li><li>Design: <a href="http://html5up.net">HTML5 UP</a>.</li>
                            <li>Created Group By: Habibie Ed Dien, Adi Purnama, Sunaryo Winardi, Sandy Gunawan.</li><hr>
                            <li><b>Final Project IF5153 - Informatics Master Degree | Institute of Technology Bandung.</b></li>
						</ul>
					</footer>

			</div>

		<!-- Scripts -->
			<script src="frontend/assets/js/jquery.min.js"></script>
			<script src="frontend/assets/js/skel.min.js"></script>
			<!--[if lte IE 8]><script src="frontend/assets/js/ie/respond.min.js"></script><![endif]-->
			<script src="frontend/assets/js/main.js"></script>
	</body>
</html>