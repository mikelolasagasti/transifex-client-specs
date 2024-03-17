# Generated by go2rpm 1.10.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/gosimple/slug
%global goipath         github.com/gosimple/slug
Version:                1.14.0

%gometa -L -f

%global common_description %{expand:
URL-friendly slugify with multiple languages support.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           golang-github-gosimple-slug
Release:        %autorelease
Summary:        URL-friendly slugify with multiple languages support

License:        MPL-2.0
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
