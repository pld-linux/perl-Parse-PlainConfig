#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Parse
%define		pnam	PlainConfig
Summary:	Parse::PlainConfig - parser for plain-text configuration files
Summary(pl):	Parse::PlainConfig - analizator czysto tekstowych plików konfiguracyjnych
Name:		perl-Parse-PlainConfig
Version:	1.7a
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	14138102429479e62fc73590452e8c51
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parse::PlainConfig provides OO objects which can parse and generate
human-readable configuration files.

%description -l pl
Parse::PlainConfig dostarcza obiekty mog±ce analizowaæ i generowaæ
czytelne dla cz³owieka pliki konfiguracyjne.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG CREDITS README
%{perl_vendorlib}/Parse/PlainConfig.pm
%{_mandir}/man3/*
