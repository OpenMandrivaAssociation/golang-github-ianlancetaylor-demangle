# Run tests in check section
%bcond_without check

%global goipath         github.com/ianlancetaylor/demangle
%global commit          4883227f66371e02c4948937d3e2be1664d9be38

%global common_description %{expand:
A Go package that can be used to demangle C++ symbol names.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        C++ symbol name demangler written in Go 
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git4883227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180417git4883227
- First package for Fedora

