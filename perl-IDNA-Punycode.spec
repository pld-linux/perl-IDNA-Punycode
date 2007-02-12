#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IDNA
%define		pnam	Punycode
Summary:	Encodes Unicode string in Punycode
Summary(pl.UTF-8):   Kodowanie ciągu znaków Unicode w Punycode
Name:		perl-IDNA-Punycode
Version:	0.02
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MI/MIYAGAWA/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e4cb6cb3f4044224475ef06f847f6667
URL:		http://search.cpan.org/dist/IDNA-Punycode/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IDNA::Punycode is a module to encode / decode Unicode strings into
Punycode, an efficient encoding of Unicode for use with IDNA.

%description -l pl.UTF-8
IDNA::Punycode jest modułem służącym do kodowania / dekodowania ciągów
znaków Unicode w Punycode, czyli wydajnym kodowaniu Unicode do użytku
z IDNA.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc Changes
%dir %{perl_vendorlib}/IDNA
%{perl_vendorlib}/IDNA/Punycode.pm
%{_mandir}/man3/*
