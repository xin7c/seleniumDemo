conf = {
	"product": {
		"getUrl": "http://devtest.adinsights.cn:9000/#/product",
		"elements":{
			"uname": "/html/body/div/div/div[1]/div[2]/ul/li[1]/input",
			"upass": "/html/body/div/div/div[1]/div[2]/ul/li[2]/input",
			"loginBtn": "html/body/div/div/div[1]/div[2]/div[4]",
			"selectDate": "/html/body/div/div/div/div/div[1]/div/span",
			"selectYesterday": "/html/body/div/div/div/div/div[1]/div/div/div[1]/a[1]",
			"trXpathGame": "/html/body/div/div/div/div/div[2]/div[1]/table/tbody/tr[%s]/td[3]"
		},
		"sendKeys":{
			"uname": "zhangliang@reyun.com",
			"upass": "reyun123",
		}
	},
	"admin": {
		"elements":{
			},
		"sendKeys":{
		}
	}
}
