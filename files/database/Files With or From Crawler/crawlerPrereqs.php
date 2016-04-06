<?php
	include("/libs/PHPCrawler.class.php");
	include_once("simple_html_dom.php"); 
	function my_callback($element){
		// if($element->tag=='a')
		// 	$element->outertext = '';
        if($element->tag=='br')
            $element->outertext = '';
        // if($element->tag=='')
        //     $element->outertext = '';
	}
	class MyCrawler extends PHPCrawler 
	{ 
	  function handleDocumentInfo(PHPCrawlerDocumentInfo $PageInfo) 
	  { 
	    // Your code comes here! 
	    // Do something with the $PageInfo-object that 
	    // contains all information about the currently  
	    // received document. 

	    // As example we just print out the URL of the document 
	    $html = new simple_html_dom();
	    $html->load_file($PageInfo->url);
	    // $html->load_file("http://catalog.iastate.edu/azcourses/an_s/");
		$html->set_callback('my_callback');
		$indexPrereq = 0;
		$index = 0;
		echo '<table>';
		foreach($html->find('div[class=courseblock]') as $post){
			$title = $html->find('div[class=courseblocktitle]', $index);
			$check = $post->children(1)->children(1)->children(0)->tag;
			if ($check == 'em'){
				$prereq = $html->find('em', $indexPrereq);
				$indexPrereq++;
				echo '<tr><td>' . $title->plaintext . '</td><td>' . $prereq->plaintext . '</td></tr>';
			}
			else
				echo '<tr><td>' . $title->plaintext . '</td><td></td></tr>';
			$index++;
    	}
    	echo '</table>';
	  } 
	}

	$crawler = new MyCrawler();
	$crawler->setURL("http://catalog.iastate.edu/azcourses/");
	$crawler->addContentTypeReceiveRule("#text/html#");
	$crawler->go();
	$report = $crawler->getProcessReport();
?>