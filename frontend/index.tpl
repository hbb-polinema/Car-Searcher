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
						<h1>Car Searcher</h1>
                        <p>search simillar photo car with your own gallery photo.</p><hr>
                        <table align="center" width="100%">
                        <tr>
                        <td>
						<select name="tahun_min">
                        	<option value="" disabled selected>Min Year</option>
						% for tahun in year:
							<option value="{{tahun}}">{{tahun}}</option>
						% end
						</select>
                        </td>
                        <td><h2> - </h2></td>
                        <td>
						<select name="tahun_max">
                        	<option value="" disabled selected>Max Year</option>
						% for tahun in year:
							<option value="{{tahun}}">{{tahun}}</option>
						% end
						</select>
                        </td>
                        </tr>
                        </table>						
						<select name="maker">
                        	<option value="" disabled selected>Select Maker</option>
						% for pembuat in maker:
							<option value="{{pembuat}}">{{pembuat}}</option>
						% end
						</select>
						
                        <!-- Form Input Query, Relevance Feedback -->
                        <form action="/search_result" method="post" enctype="multipart/form-data">
                       	<label>Select an image:</label>
                        <input type="file" name="image" required/>
                        <select id="opsi_relevance" name="opsiR" required>
                        		<option value="" disabled selected>Select Relevance</option>
							 	<option value="1">Color Dominants</option>
	 							<option value="2">Shape Dominants</option>
	 					</select>
                        
                        <div id="showRelevance">
                        	<div class="optionRelevance" id="R1">
                            	<select id="region" name="region">
                                   	<option value="" disabled selected>Select Region</option>
							 		<option value="1">All - 5 Region</option>
	 								<option value="2">Center Region Only</option>
	 							</select>
                            </div>
                            <div class="optionRelevance" id="clusterAllRegion">
	                            <select id="opsiClusterAllRegion" name="opsiClusterAllRegion">
                                   	<option value="" disabled selected>Select Clustering</option>
							 		<option value="1">No Clustering</option>
	 								<option value="35">35 Centroid</option>
                                    <option value="50">50 Centroid</option>
                                    <option value="250">250 Centroid</option>
	 							</select>
                            </div>
                            <div class="optionRelevance" id="clusterCenterRegion">
	                            <select id="opsiClusterCenterRegion" name="opsiClusterCenterRegion">
                                   	<option value="" disabled selected>Select Clustering</option>
							 		<option value="1">No Clustering</option>
	 								<option value="36">36 Centroid</option>
                                    <option value="72">72 Centroid</option>
                                    <option value="144">144 Centroid</option>
	 							</select>
                            </div>
                            <div class="optionRelevance" id="R2">
                            	<h4>content Shape</h4>
                            </div>
                        </div>
						
			  				<input type="submit" value="Start Searching"/></form>
					</header>
<hr>
				<!-- Thumbnail -->
					<section id="thumbnails">
						<article>
							<a class="thumbnail" href="/datacars/18_bentley_continental_gt_speed_2013_rear.jpg" data-position="left center"><img src="/datacars/18_bentley_continental_gt_speed_2013_rear.jpg" alt="" /></a>
							<h2>Continental GT Speed</h2>
							<p style="background-color:#000;">Sports coupe | $ 242,125 | 2013 | Bentley | Great Britain</p>
						</article>
						<article>
							<a class="thumbnail" href="/datacars/91_mercedes_benz_clk_gtr_1999_side.jpg"><img src="/datacars/91_mercedes_benz_clk_gtr_1999_side.jpg" alt="" /></a>
							<h2>CLK GTR</h2>
							<p style="background-color:#000;">Supercar | $ 1,547,620 | 1999 | Mercedes-Benz | Germany</p>
						</article>
						<article>
							<a class="thumbnail" href="/datacars/49_ford_gt90_1995_front.jpg" data-position="top center"><img src="/datacars/49_ford_gt90_1995_front.jpg" alt="" /></a>
							<h2>GT90</h2>
							<p style="background-color:#000;">Concept sports | Price: N/A | 1995 | Ford | USA</p>
						</article>
						<article>
							<a class="thumbnail" href="/datacars/18_bentley_continental_gt_speed_2013_front.jpg"><img src="/datacars/18_bentley_continental_gt_speed_2013_front.jpg" alt="" /></a>
							<h2>Continental GT Speed</h2>
							<p style="background-color:#000;">Sports coupe | $ 242,125 | 2013 | Bentley | Great Britain</p>
						</article>
						<article>
							<a class="thumbnail" href="/datacars/111_renault_alpine_a_110_50_concept_2012_rear.jpg" data-position="top center"><img src="/datacars/111_renault_alpine_a_110_50_concept_2012_rear.jpg" alt="" /></a>
							<h2>Alpine A110-50 Concept</h2>
							<p style="background-color:#000;">Concept Supercar | Price: N/A | 2012 | Renault | France</p>
						</article>
						<article>
							<a class="thumbnail" href="/datacars/51_gumpert-apollo_2008_front.jpg"><img src="/datacars/51_gumpert-apollo_2008_front.jpg" alt="" /></a>
							<h2>Apollo</h2>
							<p style="background-color:#000;">Supercar | � 275,000 | 2008 | Gumpert | Germany</p>
						</article>
						<article>
							<a class="thumbnail" href="/datacars/52_hennessey_venom_gt_2011_front.jpg"><img src="/datacars/52_hennessey_venom_gt_2011_front.jpg" alt="" /></a>
							<h2>Venom GT</h2>
							<p style="background-color:#000;">Supercar | $ 1,400,000 | 2011 | Hennessey | USA</p>
						</article>
						<article>
							<a class="thumbnail" href="/datacars/31_chrysler_crossfire_2007_rear.jpg"><img src="/datacars/31_chrysler_crossfire_2007_rear.jpg" alt="" /></a>
							<h2>Crossfire</h2>
							<p style="background-color:#000;">Sports coupe | $ 34,720 | 2007 | Chrysler | USA</p>
						</article>
						<article>
							<a class="thumbnail" href="/datacars/50_ford_mustang_gt_2015_side.jpg"><img src="/datacars/50_ford_mustang_gt_2015_side.jpg" alt="" /></a>
							<h2>Mustang GT</h2>
							<p style="background-color:#000;">Sports coupe | $ 33,295 | 2015 | Ford | USA</p>
						</article>
						<article>
							<a class="thumbnail" href="/datacars/55_italdesign_nazca_c2_1991_front.jpg"><img src="/datacars/55_italdesign_nazca_c2_1991_front.jpg" alt="" /></a>
							<h2>Nazca C2</h2>
							<p style="background-color:#000;">Concept sports | $ 1,100,000 | 1991 | Italdesign | Italy</p>
						</article>
						<article>
							<a class="thumbnail" href="/datacars/15_audi_tts_coupe_2009_side.jpg"><img src="/datacars/15_audi_tts_coupe_2009_side.jpg" alt="" /></a>
							<h2>R8 V10</h2>
							<p style="background-color:#000;">Sports coupe | � 165,000 | 2016 | Audi | Germany</p>
						</article>
						<article>
							<a class="thumbnail" href="/datacars/95_mercedes_benz_slr_stirling_moss_2009_front.jpg"><img src="/datacars/95_mercedes_benz_slr_stirling_moss_2009_front.jpg" alt="" /></a>
							<h2>SLR Stirling Moss</h2>
							<p style="background-color:#000;">FSupercar | $ 1,010,000 | 2009 | Mercedes-Benz | Germany</p>
						</article>
					</section>
<hr>
				<!-- Footer -->
					<footer id="footer">
                    	<ul class="icons">
							<li><a href="http://www.twitter.com/habibieeddien" class="icon fa-twitter"><span class="label">Twitter</span></a></li>
							<li><a href="http://www.itb.ac.id" class="icon fa-instagram"><span class="label">Instagram</span></a></li>
							<li><a href="http://github.com/habibieeddien" class="icon fa-github"><span class="label">Github</span></a></li>
							<li><a href="mailto:habibieeddien@students.itb.ac.id" class="icon fa-envelope-o"><span class="label">Email</span></a></li>
						</ul>
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
            <script>
				$(function(){
					$(".optionRelevance").hide();
					
					$("#opsi_relevance").change(function(){
						var val = $("#opsi_relevance").val();
						$(".optionRelevance").hide();
						$("#R"+val).show();
						});
						
					$("#region").change(function(){
						var val = $("#region").val();
						if(val == 1){
							$("#clusterAllRegion").show();
							$("#clusterCenterRegion").hide();
							}
						if(val == 2){
							$("#clusterCenterRegion").show();
							$("#clusterAllRegion").hide();
							}
						});
					});
            </script>

	</body>
</html>