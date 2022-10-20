run:
	python app.py

test:
	python -m pytest ./tests

test functions:
	python -m pytest ./tests/test_functions.py -sv

test order_menu:
	python -m pytest ./tests/test_order_menu.py -sv

test menu:
	python -m pytest ./tests/test_menu.py -sv

coverage:
	coverage run -m pytest ./tests

coverage pytest:
	python -m pytest ./tests -cov

connect:
	echo $WSL_HOST_IP
	export WSL_HOST_IP=$(awk '/nameserver/ { print $2 }' /etc/resolv.conf)

