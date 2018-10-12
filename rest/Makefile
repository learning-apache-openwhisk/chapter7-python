python.done:
	wsk package update python \
	&& touch python.done

utils.done:
	wsk package bind /whisk.system/utils utils \
	&& touch utils.done

restpkgs: python.done
	wsk action update python/restpkgs restpkgs.py --kind python:3

restpkgs-test: restpkgs
	wsk action invoke python/restpkgs -r

invokesort: python.done utils.done
	wsk action update python/invokesort invokesort.py --kind python:3

invokesort-test: invokesort
	wsk action invoke python/invokesort -p text "b a d a c" -r

trigger.done:
	wsk trigger create python-trigger
	touch trigger.done

firetrigger: python.done utils.done trigger.done
	wsk action update python/firetrigger firetrigger.py --kind python:3
	wsk rule update python-trigger-sort  python-trigger utils/sort

firetrigger-test: firetrigger
	wsk action invoke python/firetrigger -p text "b a d a c" -r

firewrigger-clean:
	wsk rule delete  python-trigger-sort
	wsk trigger delete python-trigger
	wsk action delete python/firetrigger
	rm trigger.done

roundtrip: python.done utils.done firetrigger
	wsk action update python/retrieve retrieve.py --kind python:3
	wsk action update python/roundtrip roundtrip.py --kind python:3

roundtrip-test: roundtrip
	wsk action invoke python/roundtrip -p text "b a d a c" -r
