# $FreeBSD$

PORTNAME=	dnscontrol
DISTVERSIONPREFIX=v
DISTVERSION=	3.3.0
CATEGORIES=	dns

MAINTAINER=	decke@FreeBSD.org
COMMENT=	Synchronize your DNS to multiple providers from a simple DSL

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

USES=		go:modules

USE_GITHUB=	yes
GH_ACCOUNT=	StackExchange

PLIST_FILES=	bin/${PORTNAME}

GH_TUPLE=	\
		Azure:azure-sdk-for-go:v46.0.0:azure_azure_sdk_for_go/vendor/github.com/Azure/azure-sdk-for-go \
		Azure:go-autorest:0529470822b5:azure_go_autorest_auth \
		Azure:go-autorest:8ac76a649a39:azure_go_autorest_cli \
		Azure:go-autorest:autorest/v0.11.4:azure_go_autorest_autorest \
		Azure:go-autorest:b3a0b30a7423:azure_go_autorest_date \
		Azure:go-autorest:cbf46deb11b5:azure_go_autorest_adal \
		Azure:go-autorest:logger/v0.2.0:azure_go_autorest_logger \
		Azure:go-autorest:tracing/v0.6.0:azure_go_autorest_tracing \
		Azure:go-autorest:v14.2.0:azure_go_autorest/vendor/github.com/Azure/go-autorest \
		DisposaBoy:JsonConfigReader:5ea4d0ddac55:disposaboy_jsonconfigreader/vendor/github.com/DisposaBoy/JsonConfigReader \
		PuerkitoBio:goquery:v1.5.1:puerkitobio_goquery/vendor/github.com/PuerkitoBio/goquery \
		TomOnTime:utfutil:0b0178852c8f:tomontime_utfutil/vendor/github.com/TomOnTime/utfutil \
		andreyvit:diff:c7f18ee00883:andreyvit_diff/vendor/github.com/andreyvit/diff \
		andybalholm:cascadia:v1.2.0:andybalholm_cascadia/vendor/github.com/andybalholm/cascadia \
		aws:aws-sdk-go:v1.34.13:aws_aws_sdk_go/vendor/github.com/aws/aws-sdk-go \
		babolivier:go-doh-client:2f86c709ac4a:babolivier_go_doh_client/vendor/github.com/babolivier/go-doh-client \
		billputer:go-namecheap:0c7adb0710f8:billputer_go_namecheap/vendor/github.com/billputer/go-namecheap \
		boombuler:barcode:6c824513bacc:boombuler_barcode/vendor/github.com/boombuler/barcode \
		cenkalti:backoff:v2.1.1:cenkalti_backoff/vendor/github.com/cenkalti/backoff \
		census-instrumentation:opencensus-go:v0.22.4:census_instrumentation_opencensus_go/vendor/go.opencensus.io \
		cpuguy83:go-md2man:v2.0.0:cpuguy83_go_md2man_v2/vendor/github.com/cpuguy83/go-md2man/v2 \
		davecgh:go-spew:v1.1.1:davecgh_go_spew/vendor/github.com/davecgh/go-spew \
		dgrijalva:jwt-go:5e25c22bd5d6:dgrijalva_jwt_go/vendor/github.com/dgrijalva/jwt-go \
		digitalocean:godo:v1.36.0:digitalocean_godo/vendor/github.com/digitalocean/godo \
		dimchansky:utfbom:v1.1.0:dimchansky_utfbom/vendor/github.com/dimchansky/utfbom \
		dnsimple:dnsimple-go:v0.62.0:dnsimple_dnsimple_go/vendor/github.com/dnsimple/dnsimple-go \
		exoscale:egoscale:v0.23.0:exoscale_egoscale/vendor/github.com/exoscale/egoscale \
		fatih:structs:v1.1.0:fatih_structs/vendor/github.com/fatih/structs \
		go-acme:lego:v2.7.2:go_acme_lego/vendor/github.com/go-acme/lego \
		go-ini:ini:v1.42.0:go_ini_ini/vendor/gopkg.in/ini.v1 \
		go-sourcemap:sourcemap:v1.0.5:go_sourcemap_sourcemap/vendor/gopkg.in/sourcemap.v1 \
		go-yaml:yaml:a5ece683394c:go_yaml_yaml_1/vendor/gopkg.in/yaml.v3 \
		go-yaml:yaml:v2.3.0:go_yaml_yaml/vendor/gopkg.in/yaml.v2 \
		gobwas:glob:e7a84e9525fe:gobwas_glob/vendor/github.com/gobwas/glob \
		gofrs:uuid:v3.2.0:gofrs_uuid/vendor/github.com/gofrs/uuid \
		golang:appengine:v1.6.6:golang_appengine/vendor/google.golang.org/appengine \
		golang:crypto:5c72a883971a:golang_crypto/vendor/golang.org/x/crypto \
		golang:groupcache:8c9f03a8e57e:golang_groupcache/vendor/github.com/golang/groupcache \
		golang:mod:v0.3.0:golang_mod/vendor/golang.org/x/mod \
		golang:net:c89045814202:golang_net/vendor/golang.org/x/net \
		golang:oauth2:bf48bf16ab8d:golang_oauth2/vendor/golang.org/x/oauth2 \
		golang:protobuf:v1.4.2:golang_protobuf/vendor/github.com/golang/protobuf \
		golang:snappy:v0.0.1:golang_snappy/vendor/github.com/golang/snappy \
		golang:sys:64077c9b5642:golang_sys/vendor/golang.org/x/sys \
		golang:text:v0.3.3:golang_text/vendor/golang.org/x/text \
		golang:time:555d28b269f0:golang_time/vendor/golang.org/x/time \
		golang:tools:5deb26317202:golang_tools/vendor/golang.org/x/tools \
		golang:xerrors:5ec99f83aff1:golang_xerrors/vendor/golang.org/x/xerrors \
		google:go-genproto:c06518451d9c:google_go_genproto/vendor/google.golang.org/genproto \
		google:go-github:v17.0.0:google_go_github/vendor/github.com/google/go-github \
		google:go-querystring:c8c88dbee036:google_go_querystring/vendor/github.com/google/go-querystring \
		googleapis:gax-go:v2.0.5:googleapis_gax_go_v2/vendor/github.com/googleapis/gax-go \
		googleapis:google-api-go-client:v0.30.0:googleapis_google_api_go_client/vendor/google.golang.org/api \
		googleapis:google-cloud-go:v0.62.0:googleapis_google_cloud_go/vendor/cloud.google.com/go \
		gopherjs:gopherjs:0766667cb4d1:gopherjs_gopherjs/vendor/github.com/gopherjs/gopherjs \
		gopherjs:jquery:73f4c7416038:gopherjs_jquery/vendor/github.com/gopherjs/jquery \
		grpc:grpc-go:v1.31.0:grpc_grpc_go/vendor/google.golang.org/grpc \
		hashicorp:errwrap:v1.0.0:hashicorp_errwrap/vendor/github.com/hashicorp/errwrap \
		hashicorp:go-cleanhttp:v0.5.1:hashicorp_go_cleanhttp/vendor/github.com/hashicorp/go-cleanhttp \
		hashicorp:go-hclog:v0.9.2:hashicorp_go_hclog/vendor/github.com/hashicorp/go-hclog \
		hashicorp:go-multierror:v1.0.0:hashicorp_go_multierror/vendor/github.com/hashicorp/go-multierror \
		hashicorp:go-retryablehttp:v0.6.3:hashicorp_go_retryablehttp/vendor/github.com/hashicorp/go-retryablehttp \
		hashicorp:go-rootcerts:v1.0.1:hashicorp_go_rootcerts/vendor/github.com/hashicorp/go-rootcerts \
		hashicorp:go-sockaddr:v1.0.2:hashicorp_go_sockaddr/vendor/github.com/hashicorp/go-sockaddr \
		hashicorp:hcl:v1.0.0:hashicorp_hcl/vendor/github.com/hashicorp/hcl \
		hashicorp:vault:api/v1.0.4:hashicorp_vault_api/vendor/github.com/hashicorp/vault \
		hashicorp:vault:sdk/v0.1.13:hashicorp_vault_sdk \
		hexonet:go-sdk:v2.2.3:hexonet_go_sdk/vendor/github.com/hexonet/go-sdk \
		jarcoal:httpmock:v1.0.4:jarcoal_httpmock/vendor/github.com/jarcoal/httpmock \
		jmespath:go-jmespath:v0.3.0:jmespath_go_jmespath/vendor/github.com/jmespath/go-jmespath \
		kolo:xmlrpc:e0350524596b:kolo_xmlrpc/vendor/github.com/kolo/xmlrpc \
		miekg:dns:v1.1.29:miekg_dns/vendor/github.com/miekg/dns \
		mitchellh:go-homedir:v1.1.0:mitchellh_go_homedir/vendor/github.com/mitchellh/go-homedir \
		mitchellh:mapstructure:v1.3.3:mitchellh_mapstructure/vendor/github.com/mitchellh/mapstructure \
		mittwald:go-powerdns:v0.4.0:mittwald_go_powerdns/vendor/github.com/mittwald/go-powerdns \
		mjibson:esc:v0.2.0:mjibson_esc/vendor/github.com/mjibson/esc \
		namedotcom:go:08470befbe04:namedotcom_go/vendor/github.com/namedotcom/go \
		nrdcg:goinwx:v0.8.1:nrdcg_goinwx/vendor/github.com/nrdcg/goinwx \
		ns1:ns1-go:c563826f4cbe:ns1_ns1_go/vendor/gopkg.in/ns1/ns1-go.v2 \
		ovh:go-ovh:ba5adb4cf014:ovh_go_ovh/vendor/github.com/ovh/go-ovh \
		philhug:opensrs-go:9dfa7433020d:philhug_opensrs_go/vendor/github.com/philhug/opensrs-go \
		pierrec:lz4:v2.0.5:pierrec_lz4/vendor/github.com/pierrec/lz4 \
		pkg:errors:v0.9.1:pkg_errors/vendor/github.com/pkg/errors \
		pmezard:go-difflib:v1.0.0:pmezard_go_difflib/vendor/github.com/pmezard/go-difflib \
		pquerna:otp:v1.2.0:pquerna_otp/vendor/github.com/pquerna/otp \
		protocolbuffers:protobuf-go:v1.25.0:protocolbuffers_protobuf_go/vendor/google.golang.org/protobuf \
		renier:xmlrpc:ce4a1a486c03:renier_xmlrpc/vendor/github.com/renier/xmlrpc \
		robertkrimen:otto:c382bd3c16ff:robertkrimen_otto/vendor/github.com/robertkrimen/otto \
		russross:blackfriday:v2.0.1:russross_blackfriday_v2/vendor/github.com/russross/blackfriday/v2 \
		ryanuber:go-glob:v1.0.0:ryanuber_go_glob/vendor/github.com/ryanuber/go-glob \
		sergi:go-diff:v1.1.0:sergi_go_diff/vendor/github.com/sergi/go-diff \
		shurcooL:sanitized_anchor_name:v1.0.0:shurcool_sanitized_anchor_name/vendor/github.com/shurcooL/sanitized_anchor_name \
		smartystreets:goconvey:68dc04aab96a:smartystreets_goconvey/vendor/github.com/smartystreets/goconvey \
		softlayer:softlayer-go:5e1c8cccc730:softlayer_softlayer_go/vendor/github.com/softlayer/softlayer-go \
		square:go-jose:v2.3.1:square_go_jose/vendor/gopkg.in/square/go-jose.v2 \
		stretchr:testify:v1.6.1:stretchr_testify/vendor/github.com/stretchr/testify \
		tdewolff:minify:v2.3.6:tdewolff_minify/vendor/github.com/tdewolff/minify \
		tdewolff:parse:v2.3.4:tdewolff_parse/vendor/github.com/tdewolff/parse \
		tdewolff:test:v1.0.6:tdewolff_test/vendor/github.com/tdewolff/test \
		tiramiseb:go-gandi:6b74caa58663:tiramiseb_go_gandi/vendor/github.com/tiramiseb/go-gandi \
		urfave:cli:v2.2.0:urfave_cli_v2/vendor/github.com/urfave/cli/v2 \
		vultr:govultr:v0.2.0:vultr_govultr/vendor/github.com/vultr/govultr

post-extract:
	@${RM} -r ${WRKSRC}/vendor/github.com/Azure/go-autorest/autorest
	@${RLN} ${WRKSRC_azure_go_autorest_autorest}/autorest ${WRKSRC}/vendor/github.com/Azure/go-autorest/autorest
	@${RM} -r ${WRKSRC}/vendor/github.com/Azure/go-autorest/autorest/adal
	@${RLN} ${WRKSRC_azure_go_autorest_adal}/autorest/adal ${WRKSRC}/vendor/github.com/Azure/go-autorest/autorest/adal
	@${RM} -r ${WRKSRC}/vendor/github.com/Azure/go-autorest/autorest/azure/auth
	@${RLN} ${WRKSRC_azure_go_autorest_auth}/autorest/azure/auth ${WRKSRC}/vendor/github.com/Azure/go-autorest/autorest/azure/auth
	@${RM} -r ${WRKSRC}/vendor/github.com/Azure/go-autorest/autorest/azure/cli
	@${RLN} ${WRKSRC_azure_go_autorest_cli}/autorest/azure/cli ${WRKSRC}/vendor/github.com/Azure/go-autorest/autorest/azure/cli
	@${RM} -r ${WRKSRC}/vendor/github.com/Azure/go-autorest/autorest/date
	@${RLN} ${WRKSRC_azure_go_autorest_date}/autorest/date ${WRKSRC}/vendor/github.com/Azure/go-autorest/autorest/date
	@${RM} -r ${WRKSRC}/vendor/github.com/Azure/go-autorest/logger
	@${RLN} ${WRKSRC_azure_go_autorest_logger}/logger ${WRKSRC}/vendor/github.com/Azure/go-autorest/logger
	@${RM} -r ${WRKSRC}/vendor/github.com/Azure/go-autorest/tracing
	@${RLN} ${WRKSRC_azure_go_autorest_tracing}/tracing ${WRKSRC}/vendor/github.com/Azure/go-autorest/tracing
	@${RM} -r ${WRKSRC}/vendor/github.com/hashicorp/vault/sdk
	@${RLN} ${WRKSRC_hashicorp_vault_sdk}/sdk ${WRKSRC}/vendor/github.com/hashicorp/vault/sdk

.include <bsd.port.mk>
