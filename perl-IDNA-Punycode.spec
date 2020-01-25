#
# Conditional build:
%bcond_with	tests	# perform "make test" (encode_w-prefix test fails)
#
%define		pdir	IDNA
%define		pnam	Punycode
Summary:	DEPRECATED module for IDNA and Punycode
Summary(pl.UTF-8):	PRZESTARZAŁY moduł do kodowania IDNA i Punycode
Name:		perl-IDNA-Punycode
Version:	1.001
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/C/CF/CFAERBER/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3052cad5a6fcd7141cf84540a6c26820
URL:		http://search.cpan.org/dist/IDNA-Punycode/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IDNA::Punycode is a module to encode / decode Unicode strings into
Punycode, an efficient encoding of Unicode for use with IDNA.

Note: this module is deprecated; it's advised use Net::IDN::Encode or
Net::IDN::Punycode instead.

%description -l pl.UTF-8
IDNA::Punycode jest modułem służącym do kodowania / dekodowania ciągów
znaków Unicode w Punycode, czyli wydajnym kodowaniu Unicode do użytku
z IDNA.

Uwaga: ten moduł jest przestarzały; zaleca się używanie modułu
Net::IDN::Encode lub Net::IDN::Punycode.

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
%doc Changes README
%dir %{perl_vendorlib}/IDNA
%{perl_vendorlib}/IDNA/Punycode.pm
%{_mandir}/man3/IDNA::Punycode.3pm*
