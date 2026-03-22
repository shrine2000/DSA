<h2><a href="https://leetcode.com/problems/design-in-memory-file-system/">588. Design In-Memory File System</a></h2><h3>Hard</h3><hr><div><p>Design a data structure that simulates an in-memory file system.</p>

<p>Implement the <code>FileSystem</code> class:</p>

<ul>
	<li><code>FileSystem()</code> Initializes the object of the system.</li>
	<li><code>List&lt;String&gt; ls(String path)</code>
	<ul>
		<li>If <code>path</code> is a file path, returns a list that only contains this file's name.</li>
		<li>If <code>path</code> is a directory path, returns the list of file and directory names <strong>in this directory</strong>.</li>
		<li>The answer should in <strong>lexicographic order</strong>.</li>
	</ul>
	</li>
	<li><code>void mkdir(String path)</code> Makes a new directory according to the given <code>path</code>. The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.</li>
	<li><code>void addContentToFile(String filePath, String content)</code>
	<ul>
		<li>If <code>filePath</code> does not exist, creates that file containing given <code>content</code>.</li>
		<li>If <code>filePath</code> already exists, appends the given <code>content</code> to original content.</li>
	</ul>
	</li>
	<li><code>String readContentFromFile(String filePath)</code> Returns the content in the file at <code>filePath</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input</strong>
["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
[[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
<strong>Output</strong>
[null, [], null, null, ["a"], "hello"]

<strong>Explanation</strong>
FileSystem fileSystem = new FileSystem();
fileSystem.ls("/");                         // return []
fileSystem.mkdir("/a/b/c");                 // Creates directories: /, /a, /a/b, /a/b/c
fileSystem.addContentToFile("/a/b/c/d", "hello"); // Creates file /a/b/c/d with content "hello"
fileSystem.ls("/");                         // return ["a"]
fileSystem.readContentFromFile("/a/b/c/d"); // return "hello"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= path.length, filePath.length &lt;= 100</code></li>
	<li><code>path</code> and <code>filePath</code> are absolute paths which begin with <code>'/'</code> and do not end with <code>'/'</code> except that the path is just <code>"/"</code>.</li>
	<li>You can assume that all directory names and file names only contain lowercase letters, and the same file or directory name will not appear in the same directory.</li>
	<li>You can assume that all operations will be valid. For example, all the directories in the <code>mkdir</code> operation will be valid.</li>
	<li><code>1 &lt;= content.length &lt;= 50</code></li>
	<li>At most <code>300</code> calls will be made to <code>ls</code>, <code>mkdir</code>, <code>addContentToFile</code>, and <code>readContentFromFile</code>.</li>
</ul>
</div>
