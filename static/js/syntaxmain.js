function path() {
    var args = arguments,
        result = []
            ;
    for(var i = 0; i < args.length; i++)
        result.push(args[i].replace('@', '/js/'));
    return result
}
SyntaxHighlighter.autoloader.apply(null, path(
        'bash           @shBrushBash.js',
        'applescript    @shBrushAppleScript.js'
));
SyntaxHighlighter.all();

