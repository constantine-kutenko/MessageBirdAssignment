
#
#
#

CHART_NAME="web-server"
RELEASE_NAME="web-server"
NAMESPACE="test"

lint:
	@helm lint ${CHART_NAME}/${CHART_NAME}

template:
	@helm template \
		--set service.externalIPs={10.1.1.254} \
        ${CHART_NAME}/${CHART_NAME}

dryrun:
	@helm install --kube-context eks --tiller-namespace kube-system --tiller-connection-timeout 15 \
		--dry-run \
		--debug \
		--name ${RELEASE_NAME} \
		${CHART_NAME}/${CHART_NAME}

install:
	@helm repo update
	@helm dependency update ${CHART_NAME}/${CHART_NAME}
	@helm install --kube-context eks --tiller-namespace kube-system --tiller-connection-timeout 15 \
		--name ${RELEASE_NAME} \
		--namespace ${NAMESPACE} \
		--set service.externalIPs={10.1.1.254} \
		REDACTED/${CHART_NAME}
	@helm ls --kube-context eks --tiller-namespace kube-system --tiller-connection-timeout 15 ${CHART_NAME}

upgrade:
	@helm repo update
	@helm dependency update ${CHART_NAME}/${CHART_NAME}
	@helm get values --kube-context eks --tiller-namespace kube-system --tiller-connection-timeout 15 --all web-server > /tmp/web-server.values
	@helm upgrade --kube-context eks --tiller-namespace kube-system --tiller-connection-timeout 15 \
		web-server \
		REDACTED/web-server \
		-f /tmp/web-server.values \
		--set service.externalIPs={10.1.1.254}
	rm -f /tmp/web-server.values
	@helm ls --kube-context eks --tiller-namespace kube-system --tiller-connection-timeout 15 ${CHART_NAME}
