%global tl_name liftarm
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.0
Release:	%{tl_revision}.1
Summary:	Geometric constructions with liftarms using TikZ and LaTeX3
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/liftarm
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/liftarm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/liftarm.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is based on the package TikZ and can be used to draw
geometric constructions with liftarms. There are several options for the
appearance of the liftarms. It provides an environment to connect
multiple liftarms using the Newton-Raphson method and LU decomposition.
It also provides a command to describe a construction and a method to
animate a construction with one or more traces.

