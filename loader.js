// List Loader JS [by: d3str0y3r]
const Loader = {}

window.addEventListener("load", () => {
	Loader.load = function(Request) {
		if(Request.status === 200) {
			try {
				const list = Request.responseText.split("\n") || Request.response.split("\n");

				for(cfgTXT of list) {
					try {
						const cfg = JSON.parse(cfgTXT);

						const element = document.createElement(cfg.name);
						document.body.appendChild(element);

						for(propClass of cfg.properties) {
							element.setAttribute(propClass[0], propClass[1]);
						}
					} catch(e) {
						console.log("[D3STR0Y3R Loader Warn]: Falha ao criar um elemento!\n"+e+"\n");
					}
				}
			} catch(e) {
				console.log("[D3STR0Y3R Loader Error]: Falha ao ler a lista!\n"+e+"\n");
			}
		} else {
			console.log("[D3STR0Y3R Loader Error]: Falha ao carregar a lista!\n");
		}
	}

	Loader.from = {
		"pastebin": function(pasteID) {
			const Request = new XMLHttpRequest();
			Request.open("GET", "https://pastebin.com/raw/"+pasteID);
			Request.onload = function() {
				Loader.load(Request);
			}
			Request.send();
		},
		"src": function(url) {
			const Request = new XMLHttpRequest();
			Request.open("GET", url);
			Request.onload = function() {
				Loader.load(Request);
			}
			Request.send();
		},
		"github": function(author, repo, file) {
			const Request = new XMLHttpRequest();
			Request.open("GET", "https://raw.githubusercontent.com/"+author+"/"+repo+"/master/"+file);
			Request.onload = function() {
				Loader.load(Request);
			}
			Request.send();
		}
	}

	if(typeof(Autoloader) === "function") {
		Autoloader(Loader);
	}
});
