DOCKERNAME = dq_home2
DOCKERIMAGE = zeromake/dq_home2:0.1
PWD = $(shell pwd)
build:
	docker build -t $(DOCKERIMAGE) .
clean:
	docker rmi $(DOCKERIMAGE)
run:
	docker run --name $(DOCKERNAME) -d -v $(PWD)/server:/data/web:rw -p 9033:9033 --restart=always -e "CONFIG_FILE=/data/web/conf/conf.json" $(DOCKERIMAGE)
restart:
	docker restart $(DOCKERNAME)
stop:
	docker stop $(DOCKERNAME)
start:
	docker start $(DOCKERNAME)
del:
	docker rm $(DOCKERNAME)
exec:
	docker exec -it $(DOCKERNAME) sh
test:
	echo "$(PWD)"
build_client:
	cd client && npm run dll && npm run dll_user
