<?php
	include("/libs/PHPCrawler.class.php");
	include_once("simple_html_dom.php"); 
	set_time_limit(10000);
	function my_callback($element){
		if($element->tag=='em')
			$element->outertext = '';
		if($element->tag=='br')
			$element->outertext = '';
		if($element->tag=='span')
			$element->outertext = '';

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
	    // $html->load_file("http://catalog.iastate.edu/azcourses/acct");
		$html->set_callback('my_callback');
		$index = 0;
		foreach($html->find('div[class=courseblocktitle]') as $post){
        	echo $post.$lb;
        	echo $html->find('p[class=prereq]')[$index];
    		$index++;
    	} 
	  } 
	}

	$crawler = new MyCrawler();
	$crawler->setURL("http://catalog.iastate.edu/azcourses");
	$crawler->addContentTypeReceiveRule("#text/html#");
	$crawler->setContentSizeLimit(1000 * 1024);
	$crawler->go();
	$report = $crawler->getProcessReport();
?>