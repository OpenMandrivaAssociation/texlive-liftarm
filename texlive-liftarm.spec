Name:		texlive-liftarm
Version:	71309
Release:	1
Summary:	Draw liftarms
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/liftarm
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/liftarm.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/liftarm.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package can be used to draw liftarms with TikZ. It
provides several options for the appearance of the liftarms, a
command which connects two liftarms and an environment to
describe a construction.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/liftarm
%doc %{_texmfdistdir}/doc/latex/liftarm

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
