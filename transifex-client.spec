# Generated by go2rpm 1.10.0
%bcond_without check

# https://github.com/transifex/cli
%global goipath         github.com/transifex/cli
Version:                1.6.10

%gometa -L -f

%global common_description %{expand:
The Transifex command-line client.}

%global golicenses      LICENSE
%global godocs          examples CODE_OF_CONDUCT.md CONTRIBUTING.md README.md

Name:           transifex-client
Release:        %autorelease
Summary:        The Transifex command-line client

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}
Patch:          0001-Remove-autoupdate-feature.patch

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/tx %{goipath}/cmd/tx

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc examples CODE_OF_CONDUCT.md CONTRIBUTING.md README.md RELEASING.md
%{_bindir}/*

%changelog
%autochangelog