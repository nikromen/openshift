# gg, very predictable tag
%global tag_suffix 202402082307
%global long_name openshift-clients

Name:           oc
Version:        4.15.0
Release:        %autorelease
Summary:        The OpenShift Command Line, part of OKD

License:        Apache-2.0
URL:            https://github.com/openshift/%{name}
Source0:        %{url}/archive/refs/tags/${long_name}-%{name}-%{tag_suffix}

BuildRequires:  make
BuildRequires:  krb5-devel
BuildRequires:  gpgme-devel
BuildRequires:  libassuan-devel


%description
With OpenShift Client CLI (oc), you can create applications and manage
OpenShift resources. It is built on top of kubectl which means it provides
its full capabilities to connect with any kubernetes compliant cluster, and
on top adds commands simplifying interaction with an OpenShift cluster.


%prep
%autosetup


%build
%configure
%make_build


%install
%make_install


%files
%license LICENSE
%doc README.md
%{_bindir}/oc


%changelog
%autochangelog

