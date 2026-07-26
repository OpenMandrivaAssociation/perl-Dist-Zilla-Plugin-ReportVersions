%define upstream_name    Dist-Zilla-Plugin-ReportVersions
Name:		perl-%{upstream_name}
Version:	1.110730
Release:	5

Summary:	Write a test that reports used module versions
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/hanekomu/Dist-Zilla-Plugin-ReportVersions
Source0:	https://cpan.metacpan.org/authors/id/M/MA/MARCEL/Dist-Zilla-Plugin-ReportVersions-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Dist::Zilla::Plugin::InlineFiles)
BuildRequires:	perl(English)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More) >= 0.940.0

BuildArch:	noarch

%description
This is an extension of the Dist::Zilla::Plugin::InlineFiles manpage,
providing the following files

  t/000-report-versions.t

The '000' prefix is chosen so it runs first to make sure it shows up in
CPAN tester reports.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml META.json README
%{_mandir}/man3/*
%{perl_vendorlib}/*


