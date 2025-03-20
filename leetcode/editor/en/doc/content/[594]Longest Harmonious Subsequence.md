<p>We define a harmonious array as an array where the difference between its maximum value and its minimum value is <b>exactly</b> <code>1</code>.</p>

<p>Given an integer array <code>nums</code>, return the length of its longest harmonious <span data-keyword="subsequence-array">subsequence</span> among all its possible subsequences.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p>

<div class="example-block"> 
 <p><strong>Input:</strong> <span class="example-io">nums = [1,3,2,2,5,2,3,7]</span></p> 
</div>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>The longest harmonious subsequence is <code>[3,2,2,2,3]</code>.</p>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block"> 
 <p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4]</span></p> 
</div>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The longest harmonious subsequences are <code>[1,2]</code>, <code>[2,3]</code>, and <code>[3,4]</code>, all of which have a length of 2.</p>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block"> 
 <p><strong>Input:</strong> <span class="example-io">nums = [1,1,1,1]</span></p> 
</div>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>No harmonic subsequence exists.</p>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li> 
 <li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li> 
</ul>

<div><div>Related Topics</div><div><li>Array</li><li>Hash Table</li><li>Sliding Window</li><li>Sorting</li><li>Counting</li></div></div><br><div><li>👍 2258</li><li>👎 294</li></div>