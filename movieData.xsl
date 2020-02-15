<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
	<html>
		<head>
			<title>Movie Database</title>
			<h1>Movie Database</h1>
		</head>
		<body>
			<xsl:apply-templates select="movies/movie"/>
		</body>
	</html>
</xsl:template>

<xsl:template match="movies/movie">
	<table border="1">
		<tr><td>Title</td><td>Actor</td><td>Director</td><td>Release</td>
		</tr>
		<tr>
			<td><xsl:value-of select="title"/></td>
			<td><xsl:value-of select="actors/actor"/></td>
			<td><xsl:value-of select="director"/></td>
			<td><xsl:value-of select="release"/></td>
		</tr>
	</table>
	<h2></h2>
</xsl:template>
</xsl:stylesheet>
