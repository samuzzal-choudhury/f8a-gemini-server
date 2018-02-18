import requests
import os

payload = {
    "result": [{
        "summary": [],
        "details": [{
            "ecosystem": "maven",
            "description": "Exposes an HTTP API using Vert.x",
            "_resolved": [{
                "package": "io.vertx:vertx-web",
                "version": "3.4.2"
            }, {
                "package": "io.vertx:vertx-core",
                "version": "3.4.2"
            }],
            "manifest_file_path": "/home/JohnDoe",
            "manifest_file": "pom.xml",
            "declared_licenses": ["Apache License, Version 2.0"],
            "name": "Vert.x - HTTP",
            "dependencies": ["io.vertx:vertx-web 3.4.2", "io.vertx:vertx-core 3.4.2"],
            "version": "1.0.0-SNAPSHOT",
            "devel_dependencies": [
                "com.jayway.restassured:rest-assured 2.9.0",
                "io.openshift:openshift-test-utils 2",
                "org.assertj:assertj-core 3.6.2", "junit:junit 4.12",
                "io.vertx:vertx-unit 3.4.2", "io.vertx:vertx-web-client 3.4.2",
                "com.jayway.awaitility:awaitility 1.7.0"], "homepage": None
        }],
        "status": "success"
    }]
}
port = os.getenv("API_BACKBONE_SERVICE_PORT", "5000")

url = "http://localhost:{port}/api/v1".format(port=port)


def test_stack_api_endpoint():
    stack_resp = requests.post(url + "/stack_aggregator", json=payload)
    jsn = stack_resp.json()
    assert(jsn['stack_aggregator'] == 'failure')
    assert(jsn['external_request_id'] is None)


def test_recommendation_api_endpoint():
    rec_resp = requests.post(url + "/recommender", json=payload)
    jsn = rec_resp.json()
    assert(jsn['recommendation'] == 'failure')
    assert(jsn['external_request_id'] is None)
