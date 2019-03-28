package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"net/url"
	"strings"
	"sync"

	"github.com/antchfx/htmlquery"
)

const classifierURL = "https://pypi.org/pypi?%3Aaction=list_classifiers"
const searchURL = "https://pypi.org/search/?q=&o=&c="

var wg = sync.WaitGroup{}

func search(classifier string) {
	doc, err := htmlquery.LoadURL(searchURL + url.QueryEscape(classifier))
	if err != nil {
		log.Fatalln(err)
		return
	}
	node := htmlquery.FindOne(doc, `//*[@id="content"]/section/div/div[2]/form/section[1]/div[1]/p/strong`)
	count := strings.Replace(htmlquery.InnerText(node), ",", "", -1)
	fmt.Println(classifier, "|", count)
	wg.Done()
}

func main() {
	resp, err := http.Get(classifierURL)
	if err != nil {
		log.Fatalln(err)
		return
	}
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatalln(err)
		return
	}
	classifiers := strings.Split(string(body), "\n")
	for _, classifier := range classifiers {
		wg.Add(1)
		go search(classifier)
	}
	wg.Wait()
}
