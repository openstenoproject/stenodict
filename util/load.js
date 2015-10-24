import 'isomorphic-fetch'

let readAsText = blob => {
	let reader = new FileReader();
	return new Promise(resolve => {
		reader.addEventListener("loadend", function() {
			resolve(reader.result)
		})
		reader.readAsText(blob)
	})
}

export function fetchJSON(url) {
	return fetch(url).then(response => {
		if (response.status !== 200) {
			throw new Error(`Unable to fetch ${url}`)
		}
		return response.blob()
	})
		.then(blob => readAsText(blob))
		.then(jsonString => JSON.parse(jsonString))
}
