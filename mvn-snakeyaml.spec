#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-snakeyaml
Version  : 1.12
Release  : 7
URL      : https://repo1.maven.org/maven2/org/yaml/snakeyaml/1.12/snakeyaml-1.12.jar
Source0  : https://repo1.maven.org/maven2/org/yaml/snakeyaml/1.12/snakeyaml-1.12.jar
Source1  : https://repo1.maven.org/maven2/org/yaml/snakeyaml/1.11/snakeyaml-1.11.jar
Source2  : https://repo1.maven.org/maven2/org/yaml/snakeyaml/1.11/snakeyaml-1.11.pom
Source3  : https://repo1.maven.org/maven2/org/yaml/snakeyaml/1.12/snakeyaml-1.12.pom
Source4  : https://repo1.maven.org/maven2/org/yaml/snakeyaml/1.14/snakeyaml-1.14.jar
Source5  : https://repo1.maven.org/maven2/org/yaml/snakeyaml/1.14/snakeyaml-1.14.pom
Source6  : https://repo1.maven.org/maven2/org/yaml/snakeyaml/1.15/snakeyaml-1.15.jar
Source7  : https://repo1.maven.org/maven2/org/yaml/snakeyaml/1.15/snakeyaml-1.15.pom
Source8  : https://repo1.maven.org/maven2/org/yaml/snakeyaml/1.16/snakeyaml-1.16.jar
Source9  : https://repo1.maven.org/maven2/org/yaml/snakeyaml/1.16/snakeyaml-1.16.pom
Source10  : https://repo1.maven.org/maven2/org/yaml/snakeyaml/1.17/snakeyaml-1.17.jar
Source11  : https://repo1.maven.org/maven2/org/yaml/snakeyaml/1.17/snakeyaml-1.17.pom
Source12  : https://repo1.maven.org/maven2/org/yaml/snakeyaml/1.23/snakeyaml-1.23.jar
Source13  : https://repo1.maven.org/maven2/org/yaml/snakeyaml/1.23/snakeyaml-1.23.pom
Source14  : https://repo1.maven.org/maven2/org/yaml/snakeyaml/1.6/snakeyaml-1.6.jar
Source15  : https://repo1.maven.org/maven2/org/yaml/snakeyaml/1.6/snakeyaml-1.6.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-snakeyaml-data = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
No detailed description available

%package data
Summary: data components for the mvn-snakeyaml package.
Group: Data

%description data
data components for the mvn-snakeyaml package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.12
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.12/snakeyaml-1.12.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.11
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.11/snakeyaml-1.11.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.11
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.11/snakeyaml-1.11.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.12
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.12/snakeyaml-1.12.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.14
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.14/snakeyaml-1.14.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.14
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.14/snakeyaml-1.14.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.15
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.15/snakeyaml-1.15.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.15
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.15/snakeyaml-1.15.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.16
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.16/snakeyaml-1.16.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.16
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.16/snakeyaml-1.16.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.17
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.17/snakeyaml-1.17.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.17
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.17/snakeyaml-1.17.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.23
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.23/snakeyaml-1.23.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.23
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.23/snakeyaml-1.23.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.6
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.6/snakeyaml-1.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.6
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.6/snakeyaml-1.6.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.11/snakeyaml-1.11.jar
/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.11/snakeyaml-1.11.pom
/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.12/snakeyaml-1.12.jar
/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.12/snakeyaml-1.12.pom
/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.14/snakeyaml-1.14.jar
/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.14/snakeyaml-1.14.pom
/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.15/snakeyaml-1.15.jar
/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.15/snakeyaml-1.15.pom
/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.16/snakeyaml-1.16.jar
/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.16/snakeyaml-1.16.pom
/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.17/snakeyaml-1.17.jar
/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.17/snakeyaml-1.17.pom
/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.23/snakeyaml-1.23.jar
/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.23/snakeyaml-1.23.pom
/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.6/snakeyaml-1.6.jar
/usr/share/java/.m2/repository/org/yaml/snakeyaml/1.6/snakeyaml-1.6.pom
