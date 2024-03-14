# gg, very predictable tag
%global tag_suffix 202402082307
%global ver 4.15.0

%global long_name openshift-clients
%global tag_name %{long_name}-%{ver}-%{tag_suffix}


Name:           oc
Version:        %{ver}
Release:        %autorelease
Summary:        The OpenShift Command Line, part of OKD

License:        Apache-2.0
URL:            https://github.com/openshift/%{name}
Source0:        %{url}/archive/refs/tags/%{tag_name}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  krb5-devel
BuildRequires:  golang
BuildRequires:  rsync

Requires:       bash-completion


%description
With OpenShift Client CLI (oc), you can create applications and manage
OpenShift resources. It is built on top of kubectl which means it provides
its full capabilities to connect with any kubernetes compliant cluster, and
on top adds commands simplifying interaction with an OpenShift cluster.


%prep
%autosetup -n %{name}-%{tag_name}


%build
make build GO_BUILD_PACKAGES:="./cmd/%{name} ./tools/genman"


%install
install -d %{buildroot}%{_bindir}
install -p -m 755 ./%{name} %{buildroot}%{_bindir}/%{name}
ln -s ./%{name} %{buildroot}%{_bindir}/kubectl

# Install man1 man pages
install -d -m 0755 %{buildroot}%{_mandir}/man1
./genman %{buildroot}%{_mandir}/man1 %{name}

# Install bash completions
install -d -m 755 %{buildroot}%{_sysconfdir}/bash_completion.d
for bin in %{name} kubectl
do
  %{buildroot}%{_bindir}/${bin} completion bash > %{buildroot}%{_sysconfdir}/bash_completion.d/${bin}
  chmod 644 %{buildroot}%{_sysconfdir}/bash_completion.d/${bin}
done


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/kubectl
%dir %{_mandir}/man1
%{_mandir}/man1/%{name}*
%{_sysconfdir}/bash_completion.d/%{name}
%{_sysconfdir}/bash_completion.d/kubectl


%changelog
%autochangelog

