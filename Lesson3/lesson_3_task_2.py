from smartphone import Smartphone

catalog = []

catalog.append(Smartphone('Apple', 'iPhone', '+79123456'))
catalog.append(Smartphone('Samsung', 'Galaxy A55', '+79234569'))
catalog.append(Smartphone('Honor', 'X8B', '+7900258'))
catalog.append(Smartphone('Philips', 'Xenium', '+79789456'))
catalog.append(Smartphone('Xiaomi', 'Redmi 13', '+79555777'))

for phone in catalog:
    print(f"{phone.phoneBrand} - {phone.phoneModel}. {phone.phoneNumber}")
