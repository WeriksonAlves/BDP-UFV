<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="7.2.0">
<drawing>
<settings>
<setting alwaysvectorfont="no"/>
<setting verticaltext="up"/>
</settings>
<grid distance="0.1" unitdist="inch" unit="inch" style="lines" multiple="1" display="no" altdistance="0.01" altunitdist="inch" altunit="inch"/>
<layers>
<layer number="1" name="Top" color="4" fill="1" visible="no" active="no"/>
<layer number="2" name="Route2" color="1" fill="3" visible="no" active="no"/>
<layer number="3" name="Route3" color="4" fill="3" visible="no" active="no"/>
<layer number="4" name="Route4" color="1" fill="4" visible="no" active="no"/>
<layer number="5" name="Route5" color="4" fill="4" visible="no" active="no"/>
<layer number="6" name="Route6" color="1" fill="8" visible="no" active="no"/>
<layer number="7" name="Route7" color="4" fill="8" visible="no" active="no"/>
<layer number="8" name="Route8" color="1" fill="2" visible="no" active="no"/>
<layer number="9" name="Route9" color="4" fill="2" visible="no" active="no"/>
<layer number="10" name="Route10" color="1" fill="7" visible="no" active="no"/>
<layer number="11" name="Route11" color="4" fill="7" visible="no" active="no"/>
<layer number="12" name="Route12" color="1" fill="5" visible="no" active="no"/>
<layer number="13" name="Route13" color="4" fill="5" visible="no" active="no"/>
<layer number="14" name="Route14" color="1" fill="6" visible="no" active="no"/>
<layer number="15" name="Route15" color="4" fill="6" visible="no" active="no"/>
<layer number="16" name="Bottom" color="1" fill="1" visible="no" active="no"/>
<layer number="17" name="Pads" color="2" fill="1" visible="no" active="no"/>
<layer number="18" name="Vias" color="2" fill="1" visible="no" active="no"/>
<layer number="19" name="Unrouted" color="6" fill="1" visible="no" active="no"/>
<layer number="20" name="Dimension" color="15" fill="1" visible="no" active="no"/>
<layer number="21" name="tPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="22" name="bPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="23" name="tOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="24" name="bOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="25" name="tNames" color="7" fill="1" visible="no" active="no"/>
<layer number="26" name="bNames" color="7" fill="1" visible="no" active="no"/>
<layer number="27" name="tValues" color="7" fill="1" visible="no" active="no"/>
<layer number="28" name="bValues" color="7" fill="1" visible="no" active="no"/>
<layer number="29" name="tStop" color="7" fill="3" visible="no" active="no"/>
<layer number="30" name="bStop" color="7" fill="6" visible="no" active="no"/>
<layer number="31" name="tCream" color="7" fill="4" visible="no" active="no"/>
<layer number="32" name="bCream" color="7" fill="5" visible="no" active="no"/>
<layer number="33" name="tFinish" color="6" fill="3" visible="no" active="no"/>
<layer number="34" name="bFinish" color="6" fill="6" visible="no" active="no"/>
<layer number="35" name="tGlue" color="7" fill="4" visible="no" active="no"/>
<layer number="36" name="bGlue" color="7" fill="5" visible="no" active="no"/>
<layer number="37" name="tTest" color="7" fill="1" visible="no" active="no"/>
<layer number="38" name="bTest" color="7" fill="1" visible="no" active="no"/>
<layer number="39" name="tKeepout" color="4" fill="11" visible="no" active="no"/>
<layer number="40" name="bKeepout" color="1" fill="11" visible="no" active="no"/>
<layer number="41" name="tRestrict" color="4" fill="10" visible="no" active="no"/>
<layer number="42" name="bRestrict" color="1" fill="10" visible="no" active="no"/>
<layer number="43" name="vRestrict" color="2" fill="10" visible="no" active="no"/>
<layer number="44" name="Drills" color="7" fill="1" visible="no" active="no"/>
<layer number="45" name="Holes" color="7" fill="1" visible="no" active="no"/>
<layer number="46" name="Milling" color="3" fill="1" visible="no" active="no"/>
<layer number="47" name="Measures" color="7" fill="1" visible="no" active="no"/>
<layer number="48" name="Document" color="7" fill="1" visible="no" active="no"/>
<layer number="49" name="Reference" color="7" fill="1" visible="no" active="no"/>
<layer number="51" name="tDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="52" name="bDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="88" name="SimResults" color="9" fill="1" visible="yes" active="yes"/>
<layer number="89" name="SimProbes" color="9" fill="1" visible="yes" active="yes"/>
<layer number="90" name="Modules" color="5" fill="1" visible="yes" active="yes"/>
<layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes"/>
<layer number="92" name="Busses" color="1" fill="1" visible="yes" active="yes"/>
<layer number="93" name="Pins" color="2" fill="1" visible="no" active="yes"/>
<layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes"/>
<layer number="95" name="Names" color="7" fill="1" visible="yes" active="yes"/>
<layer number="96" name="Values" color="7" fill="1" visible="yes" active="yes"/>
<layer number="97" name="Info" color="7" fill="1" visible="yes" active="yes"/>
<layer number="98" name="Guide" color="6" fill="1" visible="yes" active="yes"/>
</layers>
<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
<libraries>
<library name="con-lsta">
<description>&lt;b&gt;Female Headers etc.&lt;/b&gt;&lt;p&gt;
Naming:&lt;p&gt;
FE = female&lt;p&gt;
# contacts - # rows&lt;p&gt;
W = angled&lt;p&gt;
&lt;author&gt;Created by librarian@cadsoft.de&lt;/author&gt;</description>
<packages>
<package name="FE08W">
<description>&lt;b&gt;FEMALE HEADER&lt;/b&gt;</description>
<wire x1="-10.16" y1="1.016" x2="-10.16" y2="1.524" width="0.1524" layer="21"/>
<wire x1="-10.16" y1="1.524" x2="-10.16" y2="8.89" width="0.1524" layer="21"/>
<wire x1="-10.16" y1="8.89" x2="-8.001" y2="8.89" width="0.1524" layer="21"/>
<wire x1="-8.001" y1="8.89" x2="-7.62" y2="8.89" width="0.1524" layer="21"/>
<wire x1="-7.62" y1="8.89" x2="-7.239" y2="8.89" width="0.1524" layer="21"/>
<wire x1="-7.239" y1="8.89" x2="-5.461" y2="8.89" width="0.1524" layer="21"/>
<wire x1="-5.461" y1="8.89" x2="-5.08" y2="8.89" width="0.1524" layer="21"/>
<wire x1="-5.08" y1="8.89" x2="-4.699" y2="8.89" width="0.1524" layer="21"/>
<wire x1="-4.699" y1="8.89" x2="-2.921" y2="8.89" width="0.1524" layer="21"/>
<wire x1="-2.921" y1="8.89" x2="-2.54" y2="8.89" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="8.89" x2="-2.159" y2="8.89" width="0.1524" layer="21"/>
<wire x1="-2.159" y1="8.89" x2="-0.381" y2="8.89" width="0.1524" layer="21"/>
<wire x1="-0.381" y1="8.89" x2="0" y2="8.89" width="0.1524" layer="21"/>
<wire x1="0" y1="8.89" x2="0.381" y2="8.89" width="0.1524" layer="21"/>
<wire x1="0.381" y1="8.89" x2="2.159" y2="8.89" width="0.1524" layer="21"/>
<wire x1="2.54" y1="8.89" x2="2.54" y2="1.524" width="0.1524" layer="21"/>
<wire x1="-10.16" y1="1.524" x2="-8.001" y2="1.524" width="0.1524" layer="21"/>
<wire x1="-8.001" y1="1.524" x2="-7.62" y2="1.524" width="0.1524" layer="21"/>
<wire x1="-7.62" y1="1.524" x2="-7.239" y2="1.524" width="0.1524" layer="21"/>
<wire x1="-7.239" y1="1.524" x2="-5.461" y2="1.524" width="0.1524" layer="21"/>
<wire x1="-5.461" y1="1.524" x2="-5.08" y2="1.524" width="0.1524" layer="21"/>
<wire x1="-5.08" y1="1.524" x2="-4.699" y2="1.524" width="0.1524" layer="21"/>
<wire x1="-4.699" y1="1.524" x2="-2.921" y2="1.524" width="0.1524" layer="21"/>
<wire x1="-2.921" y1="1.524" x2="-2.54" y2="1.524" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="1.524" x2="-2.159" y2="1.524" width="0.1524" layer="21"/>
<wire x1="-2.159" y1="1.524" x2="-0.381" y2="1.524" width="0.1524" layer="21"/>
<wire x1="-0.381" y1="1.524" x2="0" y2="1.524" width="0.1524" layer="21"/>
<wire x1="0" y1="1.524" x2="0.381" y2="1.524" width="0.1524" layer="21"/>
<wire x1="0.381" y1="1.524" x2="2.159" y2="1.524" width="0.1524" layer="21"/>
<wire x1="2.159" y1="1.524" x2="2.54" y2="1.524" width="0.1524" layer="21"/>
<wire x1="0" y1="8.89" x2="0" y2="1.524" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="8.89" x2="-2.54" y2="1.524" width="0.1524" layer="21"/>
<wire x1="-5.08" y1="8.89" x2="-5.08" y2="1.524" width="0.1524" layer="21"/>
<wire x1="-7.62" y1="8.89" x2="-7.62" y2="1.524" width="0.1524" layer="21"/>
<wire x1="-8.001" y1="8.89" x2="-8.001" y2="1.524" width="0.0508" layer="21"/>
<wire x1="-7.239" y1="8.89" x2="-7.239" y2="1.524" width="0.0508" layer="21"/>
<wire x1="-5.461" y1="8.89" x2="-5.461" y2="1.524" width="0.0508" layer="21"/>
<wire x1="-4.699" y1="8.89" x2="-4.699" y2="1.524" width="0.0508" layer="21"/>
<wire x1="-2.921" y1="8.89" x2="-2.921" y2="1.524" width="0.0508" layer="21"/>
<wire x1="-2.159" y1="8.89" x2="-2.159" y2="1.524" width="0.0508" layer="21"/>
<wire x1="-0.381" y1="8.89" x2="-0.381" y2="1.524" width="0.0508" layer="21"/>
<wire x1="0.381" y1="8.89" x2="0.381" y2="1.524" width="0.0508" layer="21"/>
<wire x1="2.159" y1="8.89" x2="2.159" y2="1.524" width="0.1524" layer="21"/>
<wire x1="2.159" y1="8.89" x2="2.54" y2="8.89" width="0.1524" layer="21"/>
<wire x1="2.54" y1="8.89" x2="2.921" y2="8.89" width="0.1524" layer="21"/>
<wire x1="2.921" y1="8.89" x2="2.921" y2="1.524" width="0.0508" layer="21"/>
<wire x1="-10.16" y1="1.016" x2="10.16" y2="1.016" width="0.1524" layer="21"/>
<wire x1="2.921" y1="8.89" x2="4.699" y2="8.89" width="0.1524" layer="21"/>
<wire x1="5.08" y1="8.89" x2="5.08" y2="1.524" width="0.1524" layer="21"/>
<wire x1="2.54" y1="1.524" x2="2.921" y2="1.524" width="0.1524" layer="21"/>
<wire x1="2.921" y1="1.524" x2="4.699" y2="1.524" width="0.1524" layer="21"/>
<wire x1="4.699" y1="1.524" x2="5.08" y2="1.524" width="0.1524" layer="21"/>
<wire x1="4.699" y1="8.89" x2="4.699" y2="1.524" width="0.0508" layer="21"/>
<wire x1="4.699" y1="8.89" x2="5.08" y2="8.89" width="0.1524" layer="21"/>
<wire x1="5.08" y1="8.89" x2="5.461" y2="8.89" width="0.1524" layer="21"/>
<wire x1="5.461" y1="8.89" x2="7.239" y2="8.89" width="0.1524" layer="21"/>
<wire x1="7.239" y1="8.89" x2="7.62" y2="8.89" width="0.1524" layer="21"/>
<wire x1="7.62" y1="8.89" x2="7.62" y2="1.524" width="0.1524" layer="21"/>
<wire x1="5.461" y1="8.89" x2="5.461" y2="1.524" width="0.0508" layer="21"/>
<wire x1="5.08" y1="1.524" x2="5.461" y2="1.524" width="0.1524" layer="21"/>
<wire x1="5.461" y1="1.524" x2="7.239" y2="1.524" width="0.1524" layer="21"/>
<wire x1="7.239" y1="1.524" x2="7.62" y2="1.524" width="0.1524" layer="21"/>
<wire x1="7.62" y1="8.89" x2="8.001" y2="8.89" width="0.1524" layer="21"/>
<wire x1="8.001" y1="8.89" x2="10.16" y2="8.89" width="0.1524" layer="21"/>
<wire x1="10.16" y1="8.89" x2="10.16" y2="1.524" width="0.1524" layer="21"/>
<wire x1="10.16" y1="1.524" x2="10.16" y2="1.016" width="0.1524" layer="21"/>
<wire x1="7.62" y1="1.524" x2="8.001" y2="1.524" width="0.1524" layer="21"/>
<wire x1="8.001" y1="1.524" x2="10.16" y2="1.524" width="0.1524" layer="21"/>
<wire x1="8.001" y1="8.89" x2="8.001" y2="1.524" width="0.0508" layer="21"/>
<wire x1="7.239" y1="8.89" x2="7.239" y2="1.524" width="0.0508" layer="21"/>
<pad name="1" x="-8.89" y="0" drill="0.8128" shape="long" rot="R90"/>
<pad name="2" x="-6.35" y="0" drill="0.8128" shape="long" rot="R90"/>
<pad name="3" x="-3.81" y="0" drill="0.8128" shape="long" rot="R90"/>
<pad name="4" x="-1.27" y="0" drill="0.8128" shape="long" rot="R90"/>
<pad name="5" x="1.27" y="0" drill="0.8128" shape="long" rot="R90"/>
<pad name="6" x="3.81" y="0" drill="0.8128" shape="long" rot="R90"/>
<pad name="7" x="6.35" y="0" drill="0.8128" shape="long" rot="R90"/>
<pad name="8" x="8.89" y="0" drill="0.8128" shape="long" rot="R90"/>
<text x="-10.16" y="-2.54" size="1.27" layer="25" ratio="10">&gt;NAME</text>
<text x="-8.382" y="2.032" size="1.27" layer="27" ratio="10" rot="R90">&gt;VALUE</text>
<text x="-5.715" y="2.54" size="1.27" layer="21" ratio="10" rot="R90">2</text>
<text x="9.525" y="2.54" size="1.27" layer="21" ratio="10" rot="R90">8</text>
<text x="-3.175" y="2.54" size="1.27" layer="21" ratio="10" rot="R90">3</text>
<text x="-0.635" y="2.54" size="1.27" layer="21" ratio="10" rot="R90">4</text>
<text x="1.905" y="2.54" size="1.27" layer="21" ratio="10" rot="R90">5</text>
<text x="4.445" y="2.54" size="1.27" layer="21" ratio="10" rot="R90">6</text>
<text x="6.985" y="2.54" size="1.27" layer="21" ratio="10" rot="R90">7</text>
<rectangle x1="-9.144" y1="0" x2="-8.636" y2="1.016" layer="51"/>
<rectangle x1="-6.604" y1="0" x2="-6.096" y2="1.016" layer="51"/>
<rectangle x1="-4.064" y1="0" x2="-3.556" y2="1.016" layer="51"/>
<rectangle x1="-1.524" y1="0" x2="-1.016" y2="1.016" layer="51"/>
<rectangle x1="1.016" y1="0" x2="1.524" y2="1.016" layer="51"/>
<rectangle x1="3.556" y1="0" x2="4.064" y2="1.016" layer="51"/>
<rectangle x1="6.096" y1="0" x2="6.604" y2="1.016" layer="51"/>
<rectangle x1="8.636" y1="0" x2="9.144" y2="1.016" layer="51"/>
</package>
</packages>
<symbols>
<symbol name="FE08-1">
<wire x1="3.81" y1="-10.16" x2="-1.27" y2="-10.16" width="0.4064" layer="94"/>
<wire x1="1.905" y1="-1.905" x2="1.905" y2="-3.175" width="0.254" layer="94" curve="-180" cap="flat"/>
<wire x1="1.905" y1="-4.445" x2="1.905" y2="-5.715" width="0.254" layer="94" curve="-180" cap="flat"/>
<wire x1="1.905" y1="-6.985" x2="1.905" y2="-8.255" width="0.254" layer="94" curve="-180" cap="flat"/>
<wire x1="1.905" y1="3.175" x2="1.905" y2="1.905" width="0.254" layer="94" curve="-180" cap="flat"/>
<wire x1="1.905" y1="0.635" x2="1.905" y2="-0.635" width="0.254" layer="94" curve="-180" cap="flat"/>
<wire x1="1.905" y1="10.795" x2="1.905" y2="9.525" width="0.254" layer="94" curve="-180" cap="flat"/>
<wire x1="1.905" y1="8.255" x2="1.905" y2="6.985" width="0.254" layer="94" curve="-180" cap="flat"/>
<wire x1="1.905" y1="5.715" x2="1.905" y2="4.445" width="0.254" layer="94" curve="-180" cap="flat"/>
<wire x1="-1.27" y1="12.7" x2="-1.27" y2="-10.16" width="0.4064" layer="94"/>
<wire x1="3.81" y1="-10.16" x2="3.81" y2="12.7" width="0.4064" layer="94"/>
<wire x1="-1.27" y1="12.7" x2="3.81" y2="12.7" width="0.4064" layer="94"/>
<text x="-1.27" y="-12.7" size="1.778" layer="96">&gt;VALUE</text>
<text x="-1.27" y="13.462" size="1.778" layer="95">&gt;NAME</text>
<pin name="1" x="7.62" y="-7.62" visible="pad" length="middle" direction="pas" swaplevel="1" rot="R180"/>
<pin name="2" x="7.62" y="-5.08" visible="pad" length="middle" direction="pas" swaplevel="1" rot="R180"/>
<pin name="3" x="7.62" y="-2.54" visible="pad" length="middle" direction="pas" swaplevel="1" rot="R180"/>
<pin name="4" x="7.62" y="0" visible="pad" length="middle" direction="pas" swaplevel="1" rot="R180"/>
<pin name="5" x="7.62" y="2.54" visible="pad" length="middle" direction="pas" swaplevel="1" rot="R180"/>
<pin name="6" x="7.62" y="5.08" visible="pad" length="middle" direction="pas" swaplevel="1" rot="R180"/>
<pin name="7" x="7.62" y="7.62" visible="pad" length="middle" direction="pas" swaplevel="1" rot="R180"/>
<pin name="8" x="7.62" y="10.16" visible="pad" length="middle" direction="pas" swaplevel="1" rot="R180"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="FE08W" prefix="SV" uservalue="yes">
<description>&lt;b&gt;FEMALE HEADER&lt;/b&gt;</description>
<gates>
<gate name="G$1" symbol="FE08-1" x="0" y="0"/>
</gates>
<devices>
<device name="" package="FE08W">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
<connect gate="G$1" pin="3" pad="3"/>
<connect gate="G$1" pin="4" pad="4"/>
<connect gate="G$1" pin="5" pad="5"/>
<connect gate="G$1" pin="6" pad="6"/>
<connect gate="G$1" pin="7" pad="7"/>
<connect gate="G$1" pin="8" pad="8"/>
</connects>
<technologies>
<technology name="">
<attribute name="MF" value="" constant="no"/>
<attribute name="MPN" value="" constant="no"/>
<attribute name="OC_FARNELL" value="unknown" constant="no"/>
<attribute name="OC_NEWARK" value="unknown" constant="no"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="con-ml">
<description>&lt;b&gt;Harting  Connectors&lt;/b&gt;&lt;p&gt;
Low profile connectors, straight&lt;p&gt;
&lt;author&gt;Created by librarian@cadsoft.de&lt;/author&gt;</description>
<packages>
<package name="ML10L">
<description>&lt;b&gt;HARTING&lt;/b&gt;</description>
<wire x1="-6.35" y1="10.16" x2="-3.81" y2="10.16" width="0.254" layer="21"/>
<wire x1="-3.81" y1="10.16" x2="-5.08" y2="7.62" width="0.254" layer="21"/>
<wire x1="-5.08" y1="7.62" x2="-6.35" y2="10.16" width="0.254" layer="21"/>
<wire x1="2.794" y1="9.906" x2="2.794" y2="10.922" width="0.127" layer="21"/>
<wire x1="2.794" y1="9.906" x2="4.826" y2="9.906" width="0.127" layer="21"/>
<wire x1="4.826" y1="10.922" x2="4.826" y2="9.906" width="0.127" layer="21"/>
<wire x1="2.159" y1="3.683" x2="3.048" y2="3.683" width="0.127" layer="21"/>
<wire x1="3.048" y1="5.969" x2="4.572" y2="5.969" width="0.127" layer="21" curve="-180"/>
<wire x1="4.572" y1="5.969" x2="4.572" y2="4.445" width="0.127" layer="21"/>
<wire x1="4.572" y1="3.683" x2="5.969" y2="3.683" width="0.127" layer="21"/>
<wire x1="-2.159" y1="10.922" x2="-2.159" y2="4.445" width="0.127" layer="21"/>
<wire x1="-2.159" y1="10.922" x2="2.159" y2="10.922" width="0.127" layer="21"/>
<wire x1="2.159" y1="10.922" x2="2.159" y2="4.445" width="0.127" layer="21"/>
<wire x1="2.159" y1="4.445" x2="-2.159" y2="4.445" width="0.127" layer="21"/>
<wire x1="2.159" y1="3.429" x2="-2.159" y2="3.429" width="0.127" layer="21"/>
<wire x1="-2.159" y1="4.445" x2="-2.159" y2="3.429" width="0.127" layer="21"/>
<wire x1="2.159" y1="4.445" x2="2.159" y2="3.683" width="0.127" layer="21"/>
<wire x1="2.159" y1="3.683" x2="2.159" y2="3.429" width="0.127" layer="21"/>
<wire x1="2.159" y1="3.429" x2="2.159" y2="2.159" width="0.127" layer="21"/>
<wire x1="3.048" y1="5.969" x2="3.048" y2="4.445" width="0.127" layer="21"/>
<wire x1="3.048" y1="4.445" x2="3.048" y2="3.683" width="0.127" layer="21"/>
<wire x1="3.048" y1="4.445" x2="4.572" y2="4.445" width="0.127" layer="21"/>
<wire x1="4.572" y1="4.445" x2="4.572" y2="3.683" width="0.127" layer="21"/>
<wire x1="5.969" y1="3.683" x2="5.969" y2="10.922" width="0.127" layer="21"/>
<wire x1="5.969" y1="3.683" x2="5.969" y2="2.032" width="0.127" layer="21"/>
<wire x1="-5.715" y1="2.032" x2="-4.445" y2="2.032" width="0.127" layer="51"/>
<wire x1="-4.445" y1="2.032" x2="-3.175" y2="2.032" width="0.127" layer="21"/>
<wire x1="-3.175" y1="2.032" x2="-1.905" y2="2.032" width="0.127" layer="51"/>
<wire x1="-1.905" y1="2.032" x2="-0.635" y2="2.032" width="0.127" layer="21"/>
<wire x1="-0.635" y1="2.032" x2="0.635" y2="2.032" width="0.127" layer="51"/>
<wire x1="0.635" y1="2.032" x2="1.905" y2="2.032" width="0.127" layer="21"/>
<wire x1="1.905" y1="2.032" x2="2.159" y2="2.032" width="0.127" layer="51"/>
<wire x1="3.175" y1="2.032" x2="4.445" y2="2.032" width="0.127" layer="21"/>
<wire x1="5.715" y1="2.032" x2="4.445" y2="2.032" width="0.127" layer="51"/>
<wire x1="0" y1="10.033" x2="0" y2="10.287" width="0.508" layer="21"/>
<wire x1="6.731" y1="4.445" x2="9.525" y2="4.445" width="0.127" layer="21"/>
<wire x1="9.525" y1="4.445" x2="9.525" y2="8.255" width="0.127" layer="21"/>
<wire x1="6.731" y1="8.255" x2="9.525" y2="8.255" width="0.127" layer="21"/>
<wire x1="6.731" y1="8.255" x2="6.731" y2="4.445" width="0.127" layer="21"/>
<wire x1="2.159" y1="10.922" x2="10.16" y2="10.922" width="0.127" layer="21"/>
<wire x1="10.16" y1="10.922" x2="10.16" y2="2.032" width="0.127" layer="21"/>
<wire x1="10.16" y1="2.032" x2="9.017" y2="2.032" width="0.127" layer="21"/>
<wire x1="-2.159" y1="10.922" x2="-10.16" y2="10.922" width="0.127" layer="21"/>
<wire x1="-10.16" y1="2.032" x2="-10.16" y2="10.922" width="0.127" layer="21"/>
<wire x1="-10.16" y1="2.032" x2="-9.017" y2="2.032" width="0.127" layer="21"/>
<wire x1="5.969" y1="2.032" x2="5.715" y2="2.032" width="0.127" layer="21"/>
<wire x1="2.159" y1="2.159" x2="2.159" y2="2.032" width="0.127" layer="51"/>
<wire x1="2.159" y1="2.032" x2="3.175" y2="2.032" width="0.127" layer="51"/>
<wire x1="8.001" y1="2.032" x2="8.001" y2="1.397" width="0.127" layer="21"/>
<wire x1="9.017" y1="1.397" x2="8.001" y2="1.397" width="0.127" layer="21"/>
<wire x1="9.017" y1="1.397" x2="9.017" y2="2.032" width="0.127" layer="21"/>
<wire x1="8.001" y1="2.032" x2="5.969" y2="2.032" width="0.127" layer="21"/>
<wire x1="9.017" y1="2.032" x2="8.001" y2="2.032" width="0.127" layer="21"/>
<wire x1="-9.017" y1="2.032" x2="-9.017" y2="1.397" width="0.127" layer="21"/>
<wire x1="-9.017" y1="2.032" x2="-8.001" y2="2.032" width="0.127" layer="21"/>
<wire x1="-8.001" y1="1.397" x2="-9.017" y2="1.397" width="0.127" layer="21"/>
<wire x1="-8.001" y1="1.397" x2="-8.001" y2="2.032" width="0.127" layer="21"/>
<wire x1="-8.001" y1="2.032" x2="-5.715" y2="2.032" width="0.127" layer="21"/>
<pad name="1" x="-5.08" y="-1.27" drill="0.9144" shape="octagon"/>
<pad name="2" x="-5.08" y="1.27" drill="0.9144" shape="octagon"/>
<pad name="3" x="-2.54" y="-1.27" drill="0.9144" shape="octagon"/>
<pad name="4" x="-2.54" y="1.27" drill="0.9144" shape="octagon"/>
<pad name="5" x="0" y="-1.27" drill="0.9144" shape="octagon"/>
<pad name="6" x="0" y="1.27" drill="0.9144" shape="octagon"/>
<pad name="7" x="2.54" y="-1.27" drill="0.9144" shape="octagon"/>
<pad name="8" x="2.54" y="1.27" drill="0.9144" shape="octagon"/>
<pad name="9" x="5.08" y="-1.27" drill="0.9144" shape="octagon"/>
<pad name="10" x="5.08" y="1.27" drill="0.9144" shape="octagon"/>
<text x="-7.1628" y="-1.6764" size="1.27" layer="21" ratio="10">1</text>
<text x="-7.1882" y="0.3556" size="1.27" layer="21" ratio="10">2</text>
<text x="-10.1854" y="11.43" size="1.778" layer="25" ratio="10">&gt;NAME</text>
<text x="-0.0254" y="11.43" size="1.778" layer="27" ratio="10">&gt;VALUE</text>
<text x="8.89" y="5.08" size="1.524" layer="21" ratio="10" rot="R90">10</text>
<rectangle x1="-0.254" y1="4.445" x2="0.254" y2="10.287" layer="21"/>
<rectangle x1="-6.223" y1="9.652" x2="-3.937" y2="10.16" layer="21"/>
<rectangle x1="-5.969" y1="9.144" x2="-4.191" y2="9.652" layer="21"/>
<rectangle x1="-5.715" y1="8.636" x2="-4.445" y2="9.144" layer="21"/>
<rectangle x1="-5.461" y1="8.128" x2="-4.699" y2="8.636" layer="21"/>
<rectangle x1="-5.207" y1="7.874" x2="-4.953" y2="8.128" layer="21"/>
<rectangle x1="-5.334" y1="-0.381" x2="-4.826" y2="0.381" layer="21"/>
<rectangle x1="-5.334" y1="0.381" x2="-4.826" y2="2.032" layer="51"/>
<rectangle x1="-5.334" y1="-1.524" x2="-4.826" y2="-0.381" layer="51"/>
<rectangle x1="-2.794" y1="0.381" x2="-2.286" y2="2.032" layer="51"/>
<rectangle x1="-2.794" y1="-0.381" x2="-2.286" y2="0.381" layer="21"/>
<rectangle x1="-2.794" y1="-1.524" x2="-2.286" y2="-0.381" layer="51"/>
<rectangle x1="-0.254" y1="0.381" x2="0.254" y2="2.032" layer="51"/>
<rectangle x1="-0.254" y1="-0.381" x2="0.254" y2="0.381" layer="21"/>
<rectangle x1="-0.254" y1="-1.524" x2="0.254" y2="-0.381" layer="51"/>
<rectangle x1="2.286" y1="0.381" x2="2.794" y2="2.032" layer="51"/>
<rectangle x1="2.286" y1="-0.381" x2="2.794" y2="0.381" layer="21"/>
<rectangle x1="2.286" y1="-1.524" x2="2.794" y2="-0.381" layer="51"/>
<rectangle x1="4.826" y1="0.381" x2="5.334" y2="2.032" layer="51"/>
<rectangle x1="4.826" y1="-0.381" x2="5.334" y2="0.381" layer="21"/>
<rectangle x1="4.826" y1="-1.524" x2="5.334" y2="-0.381" layer="51"/>
</package>
</packages>
<symbols>
<symbol name="10P">
<wire x1="3.81" y1="-7.62" x2="-3.81" y2="-7.62" width="0.4064" layer="94"/>
<wire x1="-3.81" y1="7.62" x2="-3.81" y2="-7.62" width="0.4064" layer="94"/>
<wire x1="3.81" y1="-7.62" x2="3.81" y2="7.62" width="0.4064" layer="94"/>
<wire x1="-3.81" y1="7.62" x2="3.81" y2="7.62" width="0.4064" layer="94"/>
<wire x1="1.27" y1="5.08" x2="2.54" y2="5.08" width="0.6096" layer="94"/>
<wire x1="1.27" y1="2.54" x2="2.54" y2="2.54" width="0.6096" layer="94"/>
<wire x1="1.27" y1="0" x2="2.54" y2="0" width="0.6096" layer="94"/>
<wire x1="1.27" y1="-2.54" x2="2.54" y2="-2.54" width="0.6096" layer="94"/>
<wire x1="1.27" y1="-5.08" x2="2.54" y2="-5.08" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="5.08" x2="-1.27" y2="5.08" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="2.54" x2="-1.27" y2="2.54" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="0" x2="-1.27" y2="0" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="-2.54" x2="-1.27" y2="-2.54" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="-5.08" x2="-1.27" y2="-5.08" width="0.6096" layer="94"/>
<text x="-3.81" y="-10.16" size="1.778" layer="96">&gt;VALUE</text>
<text x="-3.81" y="8.382" size="1.778" layer="95">&gt;NAME</text>
<pin name="1" x="7.62" y="-5.08" visible="pad" length="middle" direction="pas" rot="R180"/>
<pin name="2" x="-7.62" y="-5.08" visible="pad" length="middle" direction="pas"/>
<pin name="3" x="7.62" y="-2.54" visible="pad" length="middle" direction="pas" rot="R180"/>
<pin name="4" x="-7.62" y="-2.54" visible="pad" length="middle" direction="pas"/>
<pin name="5" x="7.62" y="0" visible="pad" length="middle" direction="pas" rot="R180"/>
<pin name="6" x="-7.62" y="0" visible="pad" length="middle" direction="pas"/>
<pin name="7" x="7.62" y="2.54" visible="pad" length="middle" direction="pas" rot="R180"/>
<pin name="8" x="-7.62" y="2.54" visible="pad" length="middle" direction="pas"/>
<pin name="9" x="7.62" y="5.08" visible="pad" length="middle" direction="pas" rot="R180"/>
<pin name="10" x="-7.62" y="5.08" visible="pad" length="middle" direction="pas"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="ML10L" prefix="SV" uservalue="yes">
<description>&lt;b&gt;HARTING&lt;/b&gt;</description>
<gates>
<gate name="1" symbol="10P" x="0" y="0"/>
</gates>
<devices>
<device name="" package="ML10L">
<connects>
<connect gate="1" pin="1" pad="1"/>
<connect gate="1" pin="10" pad="10"/>
<connect gate="1" pin="2" pad="2"/>
<connect gate="1" pin="3" pad="3"/>
<connect gate="1" pin="4" pad="4"/>
<connect gate="1" pin="5" pad="5"/>
<connect gate="1" pin="6" pad="6"/>
<connect gate="1" pin="7" pad="7"/>
<connect gate="1" pin="8" pad="8"/>
<connect gate="1" pin="9" pad="9"/>
</connects>
<technologies>
<technology name="">
<attribute name="MF" value="" constant="no"/>
<attribute name="MPN" value="" constant="no"/>
<attribute name="OC_FARNELL" value="unknown" constant="no"/>
<attribute name="OC_NEWARK" value="unknown" constant="no"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="con-lstb">
<description>&lt;b&gt;Pin Headers&lt;/b&gt;&lt;p&gt;
Naming:&lt;p&gt;
MA = male&lt;p&gt;
# contacts - # rows&lt;p&gt;
W = angled&lt;p&gt;
&lt;author&gt;Created by librarian@cadsoft.de&lt;/author&gt;</description>
<packages>
<package name="MA05-2">
<description>&lt;b&gt;PIN HEADER&lt;/b&gt;</description>
<wire x1="-5.715" y1="2.54" x2="-4.445" y2="2.54" width="0.1524" layer="21"/>
<wire x1="-4.445" y1="2.54" x2="-3.81" y2="1.905" width="0.1524" layer="21"/>
<wire x1="-3.81" y1="1.905" x2="-3.175" y2="2.54" width="0.1524" layer="21"/>
<wire x1="-3.175" y1="2.54" x2="-1.905" y2="2.54" width="0.1524" layer="21"/>
<wire x1="-1.905" y1="2.54" x2="-1.27" y2="1.905" width="0.1524" layer="21"/>
<wire x1="-5.715" y1="2.54" x2="-6.35" y2="1.905" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="1.905" x2="-0.635" y2="2.54" width="0.1524" layer="21"/>
<wire x1="-0.635" y1="2.54" x2="0.635" y2="2.54" width="0.1524" layer="21"/>
<wire x1="0.635" y1="2.54" x2="1.27" y2="1.905" width="0.1524" layer="21"/>
<wire x1="1.905" y1="2.54" x2="3.175" y2="2.54" width="0.1524" layer="21"/>
<wire x1="3.175" y1="2.54" x2="3.81" y2="1.905" width="0.1524" layer="21"/>
<wire x1="3.81" y1="1.905" x2="4.445" y2="2.54" width="0.1524" layer="21"/>
<wire x1="4.445" y1="2.54" x2="5.715" y2="2.54" width="0.1524" layer="21"/>
<wire x1="1.905" y1="2.54" x2="1.27" y2="1.905" width="0.1524" layer="21"/>
<wire x1="-3.81" y1="-1.905" x2="-4.445" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="-1.905" x2="-1.905" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-1.905" y1="-2.54" x2="-3.175" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-3.175" y1="-2.54" x2="-3.81" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-6.35" y1="1.905" x2="-6.35" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-6.35" y1="-1.905" x2="-5.715" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-4.445" y1="-2.54" x2="-5.715" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="1.27" y1="-1.905" x2="0.635" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="0.635" y1="-2.54" x2="-0.635" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-0.635" y1="-2.54" x2="-1.27" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="3.81" y1="-1.905" x2="3.175" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="5.715" y1="-2.54" x2="4.445" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="4.445" y1="-2.54" x2="3.81" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="1.27" y1="-1.905" x2="1.905" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="3.175" y1="-2.54" x2="1.905" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="6.35" y1="1.905" x2="6.35" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="5.715" y1="2.54" x2="6.35" y2="1.905" width="0.1524" layer="21"/>
<wire x1="6.35" y1="-1.905" x2="5.715" y2="-2.54" width="0.1524" layer="21"/>
<pad name="1" x="-5.08" y="-1.27" drill="1.016" shape="octagon"/>
<pad name="3" x="-2.54" y="-1.27" drill="1.016" shape="octagon"/>
<pad name="5" x="0" y="-1.27" drill="1.016" shape="octagon"/>
<pad name="7" x="2.54" y="-1.27" drill="1.016" shape="octagon"/>
<pad name="9" x="5.08" y="-1.27" drill="1.016" shape="octagon"/>
<pad name="2" x="-5.08" y="1.27" drill="1.016" shape="octagon"/>
<pad name="4" x="-2.54" y="1.27" drill="1.016" shape="octagon"/>
<pad name="6" x="0" y="1.27" drill="1.016" shape="octagon"/>
<pad name="8" x="2.54" y="1.27" drill="1.016" shape="octagon"/>
<pad name="10" x="5.08" y="1.27" drill="1.016" shape="octagon"/>
<text x="-5.588" y="-4.191" size="1.27" layer="21" ratio="10">1</text>
<text x="-6.35" y="2.921" size="1.27" layer="25" ratio="10">&gt;NAME</text>
<text x="0" y="-4.191" size="1.27" layer="27" ratio="10">&gt;VALUE</text>
<text x="4.572" y="2.921" size="1.27" layer="21" ratio="10">10</text>
<rectangle x1="-2.794" y1="-1.524" x2="-2.286" y2="-1.016" layer="51"/>
<rectangle x1="-5.334" y1="-1.524" x2="-4.826" y2="-1.016" layer="51"/>
<rectangle x1="-0.254" y1="-1.524" x2="0.254" y2="-1.016" layer="51"/>
<rectangle x1="4.826" y1="-1.524" x2="5.334" y2="-1.016" layer="51"/>
<rectangle x1="2.286" y1="-1.524" x2="2.794" y2="-1.016" layer="51"/>
<rectangle x1="-5.334" y1="1.016" x2="-4.826" y2="1.524" layer="51"/>
<rectangle x1="-2.794" y1="1.016" x2="-2.286" y2="1.524" layer="51"/>
<rectangle x1="-0.254" y1="1.016" x2="0.254" y2="1.524" layer="51"/>
<rectangle x1="2.286" y1="1.016" x2="2.794" y2="1.524" layer="51"/>
<rectangle x1="4.826" y1="1.016" x2="5.334" y2="1.524" layer="51"/>
</package>
</packages>
<symbols>
<symbol name="MA05-2">
<wire x1="3.81" y1="-7.62" x2="-3.81" y2="-7.62" width="0.4064" layer="94"/>
<wire x1="1.27" y1="0" x2="2.54" y2="0" width="0.6096" layer="94"/>
<wire x1="1.27" y1="-2.54" x2="2.54" y2="-2.54" width="0.6096" layer="94"/>
<wire x1="1.27" y1="-5.08" x2="2.54" y2="-5.08" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="0" x2="-1.27" y2="0" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="-2.54" x2="-1.27" y2="-2.54" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="-5.08" x2="-1.27" y2="-5.08" width="0.6096" layer="94"/>
<wire x1="-3.81" y1="7.62" x2="-3.81" y2="-7.62" width="0.4064" layer="94"/>
<wire x1="3.81" y1="-7.62" x2="3.81" y2="7.62" width="0.4064" layer="94"/>
<wire x1="-3.81" y1="7.62" x2="3.81" y2="7.62" width="0.4064" layer="94"/>
<wire x1="1.27" y1="5.08" x2="2.54" y2="5.08" width="0.6096" layer="94"/>
<wire x1="1.27" y1="2.54" x2="2.54" y2="2.54" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="5.08" x2="-1.27" y2="5.08" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="2.54" x2="-1.27" y2="2.54" width="0.6096" layer="94"/>
<text x="-3.81" y="-10.16" size="1.778" layer="96">&gt;VALUE</text>
<text x="-3.81" y="8.382" size="1.778" layer="95">&gt;NAME</text>
<pin name="1" x="7.62" y="-5.08" visible="pad" length="middle" direction="pas" swaplevel="1" rot="R180"/>
<pin name="3" x="7.62" y="-2.54" visible="pad" length="middle" direction="pas" swaplevel="1" rot="R180"/>
<pin name="5" x="7.62" y="0" visible="pad" length="middle" direction="pas" swaplevel="1" rot="R180"/>
<pin name="2" x="-7.62" y="-5.08" visible="pad" length="middle" direction="pas" swaplevel="1"/>
<pin name="4" x="-7.62" y="-2.54" visible="pad" length="middle" direction="pas" swaplevel="1"/>
<pin name="6" x="-7.62" y="0" visible="pad" length="middle" direction="pas" swaplevel="1"/>
<pin name="7" x="7.62" y="2.54" visible="pad" length="middle" direction="pas" swaplevel="1" rot="R180"/>
<pin name="9" x="7.62" y="5.08" visible="pad" length="middle" direction="pas" swaplevel="1" rot="R180"/>
<pin name="8" x="-7.62" y="2.54" visible="pad" length="middle" direction="pas" swaplevel="1"/>
<pin name="10" x="-7.62" y="5.08" visible="pad" length="middle" direction="pas" swaplevel="1"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="MA05-2" prefix="SV" uservalue="yes">
<description>&lt;b&gt;PIN HEADER&lt;/b&gt;</description>
<gates>
<gate name="G$1" symbol="MA05-2" x="0" y="0"/>
</gates>
<devices>
<device name="" package="MA05-2">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="10" pad="10"/>
<connect gate="G$1" pin="2" pad="2"/>
<connect gate="G$1" pin="3" pad="3"/>
<connect gate="G$1" pin="4" pad="4"/>
<connect gate="G$1" pin="5" pad="5"/>
<connect gate="G$1" pin="6" pad="6"/>
<connect gate="G$1" pin="7" pad="7"/>
<connect gate="G$1" pin="8" pad="8"/>
<connect gate="G$1" pin="9" pad="9"/>
</connects>
<technologies>
<technology name="">
<attribute name="MF" value="" constant="no"/>
<attribute name="MPN" value="" constant="no"/>
<attribute name="OC_FARNELL" value="unknown" constant="no"/>
<attribute name="OC_NEWARK" value="unknown" constant="no"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
</libraries>
<attributes>
</attributes>
<variantdefs>
</variantdefs>
<classes>
<class number="0" name="default" width="0" drill="0">
</class>
</classes>
<parts>
<part name="PH-ESQ" library="con-lsta" deviceset="FE08W" device=""/>
<part name="PH-DIR" library="con-lsta" deviceset="FE08W" device=""/>
<part name="B=M2" library="con-ml" deviceset="ML10L" device=""/>
<part name="A=M1" library="con-ml" deviceset="ML10L" device=""/>
<part name="CON-AR-1" library="con-lstb" deviceset="MA05-2" device=""/>
<part name="CON-AR-2" library="con-lstb" deviceset="MA05-2" device=""/>
<part name="CON-IN" library="con-lstb" deviceset="MA05-2" device=""/>
</parts>
<sheets>
<sheet>
<plain>
</plain>
<instances>
<instance part="PH-ESQ" gate="G$1" x="2.54" y="60.96" smashed="yes" rot="R180">
<attribute name="VALUE" x="3.81" y="73.66" size="1.778" layer="96" rot="R180"/>
<attribute name="NAME" x="3.81" y="47.498" size="1.778" layer="95" rot="R180"/>
</instance>
<instance part="PH-DIR" gate="G$1" x="30.48" y="60.96" smashed="yes" rot="MR180">
<attribute name="VALUE" x="29.21" y="73.66" size="1.778" layer="96" rot="MR180"/>
<attribute name="NAME" x="29.21" y="47.498" size="1.778" layer="95" rot="MR180"/>
</instance>
<instance part="B=M2" gate="1" x="66.04" y="63.5" smashed="yes" rot="R180">
<attribute name="VALUE" x="69.85" y="73.66" size="1.778" layer="96" rot="R180"/>
<attribute name="NAME" x="69.85" y="55.118" size="1.778" layer="95" rot="R180"/>
</instance>
<instance part="A=M1" gate="1" x="-33.02" y="63.5" smashed="yes" rot="R180">
<attribute name="VALUE" x="-29.21" y="73.66" size="1.778" layer="96" rot="R180"/>
<attribute name="NAME" x="-29.21" y="55.118" size="1.778" layer="95" rot="R180"/>
</instance>
<instance part="CON-AR-1" gate="G$1" x="-15.24" y="88.9" smashed="yes" rot="R90">
<attribute name="VALUE" x="-5.08" y="85.09" size="1.778" layer="96" rot="R90"/>
<attribute name="NAME" x="-23.622" y="85.09" size="1.778" layer="95" rot="R90"/>
</instance>
<instance part="CON-AR-2" gate="G$1" x="45.72" y="88.9" smashed="yes" rot="R90">
<attribute name="VALUE" x="55.88" y="85.09" size="1.778" layer="96" rot="R90"/>
<attribute name="NAME" x="37.338" y="85.09" size="1.778" layer="95" rot="R90"/>
</instance>
<instance part="CON-IN" gate="G$1" x="17.78" y="63.5" smashed="yes" rot="R90">
<attribute name="VALUE" x="27.94" y="59.69" size="1.778" layer="96" rot="R90"/>
<attribute name="NAME" x="9.398" y="59.69" size="1.778" layer="95" rot="R90"/>
</instance>
</instances>
<busses>
</busses>
<nets>
<net name="V0" class="0">
<segment>
<pinref part="PH-ESQ" gate="G$1" pin="1"/>
<wire x1="-5.08" y1="68.58" x2="-12.7" y2="68.58" width="0.1524" layer="91"/>
<label x="-12.7" y="68.58" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="CON-IN" gate="G$1" pin="9"/>
<wire x1="12.7" y1="71.12" x2="12.7" y2="78.74" width="0.1524" layer="91"/>
<label x="12.7" y="73.66" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="CON-IN" gate="G$1" pin="10"/>
<wire x1="12.7" y1="55.88" x2="12.7" y2="48.26" width="0.1524" layer="91"/>
<label x="12.7" y="53.34" size="1.778" layer="95"/>
</segment>
</net>
<net name="5V" class="0">
<segment>
<pinref part="PH-ESQ" gate="G$1" pin="2"/>
<wire x1="-5.08" y1="66.04" x2="-12.7" y2="66.04" width="0.1524" layer="91"/>
<label x="-12.7" y="66.04" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="PH-DIR" gate="G$1" pin="4"/>
<wire x1="38.1" y1="60.96" x2="45.72" y2="60.96" width="0.1524" layer="91"/>
<label x="38.1" y="60.96" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="CON-IN" gate="G$1" pin="6"/>
<wire x1="17.78" y1="55.88" x2="17.78" y2="48.26" width="0.1524" layer="91"/>
<label x="17.78" y="53.34" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="CON-IN" gate="G$1" pin="5"/>
<wire x1="17.78" y1="71.12" x2="17.78" y2="78.74" width="0.1524" layer="91"/>
<label x="17.78" y="73.66" size="1.778" layer="95"/>
</segment>
</net>
<net name="GND" class="0">
<segment>
<pinref part="PH-ESQ" gate="G$1" pin="3"/>
<wire x1="-5.08" y1="63.5" x2="-12.7" y2="63.5" width="0.1524" layer="91"/>
<label x="-12.7" y="63.5" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="PH-ESQ" gate="G$1" pin="8"/>
<wire x1="-5.08" y1="50.8" x2="-12.7" y2="50.8" width="0.1524" layer="91"/>
<label x="-12.7" y="50.8" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="PH-DIR" gate="G$1" pin="8"/>
<wire x1="38.1" y1="50.8" x2="45.72" y2="50.8" width="0.1524" layer="91"/>
<label x="38.1" y="50.8" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="CON-IN" gate="G$1" pin="1"/>
<wire x1="22.86" y1="71.12" x2="22.86" y2="78.74" width="0.1524" layer="91"/>
<label x="22.86" y="73.66" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="CON-IN" gate="G$1" pin="2"/>
<wire x1="22.86" y1="55.88" x2="22.86" y2="48.26" width="0.1524" layer="91"/>
<label x="22.86" y="53.34" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="B=M2" gate="1" pin="9"/>
<wire x1="58.42" y1="58.42" x2="50.8" y2="58.42" width="0.1524" layer="91"/>
<label x="50.8" y="58.42" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="B=M2" gate="1" pin="10"/>
<wire x1="73.66" y1="58.42" x2="81.28" y2="58.42" width="0.1524" layer="91"/>
<label x="73.66" y="58.42" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="A=M1" gate="1" pin="9"/>
<wire x1="-40.64" y1="58.42" x2="-48.26" y2="58.42" width="0.1524" layer="91"/>
<label x="-48.26" y="58.42" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="A=M1" gate="1" pin="10"/>
<wire x1="-25.4" y1="58.42" x2="-17.78" y2="58.42" width="0.1524" layer="91"/>
<label x="-25.4" y="58.42" size="1.778" layer="95"/>
</segment>
</net>
<net name="D5" class="0">
<segment>
<pinref part="PH-DIR" gate="G$1" pin="1"/>
<wire x1="38.1" y1="68.58" x2="45.72" y2="68.58" width="0.1524" layer="91"/>
<label x="38.1" y="68.58" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="CON-AR-2" gate="G$1" pin="1"/>
<wire x1="50.8" y1="96.52" x2="50.8" y2="104.14" width="0.1524" layer="91"/>
<label x="50.8" y="99.06" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="CON-AR-2" gate="G$1" pin="2"/>
<wire x1="50.8" y1="81.28" x2="50.8" y2="73.66" width="0.1524" layer="91"/>
<label x="50.8" y="78.74" size="1.778" layer="95"/>
</segment>
</net>
<net name="RX0" class="0">
<segment>
<pinref part="PH-DIR" gate="G$1" pin="2"/>
<wire x1="38.1" y1="66.04" x2="45.72" y2="66.04" width="0.1524" layer="91"/>
<label x="38.1" y="66.04" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="CON-AR-2" gate="G$1" pin="6"/>
<wire x1="45.72" y1="81.28" x2="45.72" y2="73.66" width="0.1524" layer="91"/>
<label x="45.72" y="76.2" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="CON-AR-2" gate="G$1" pin="5"/>
<wire x1="45.72" y1="96.52" x2="45.72" y2="104.14" width="0.1524" layer="91"/>
<label x="45.72" y="101.6" size="1.778" layer="95"/>
</segment>
</net>
<net name="TX1" class="0">
<segment>
<pinref part="PH-DIR" gate="G$1" pin="3"/>
<wire x1="38.1" y1="63.5" x2="45.72" y2="63.5" width="0.1524" layer="91"/>
<label x="38.1" y="63.5" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="CON-AR-2" gate="G$1" pin="9"/>
<wire x1="40.64" y1="96.52" x2="40.64" y2="104.14" width="0.1524" layer="91"/>
<label x="40.64" y="99.06" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="CON-AR-2" gate="G$1" pin="10"/>
<wire x1="40.64" y1="81.28" x2="40.64" y2="73.66" width="0.1524" layer="91"/>
<label x="40.64" y="78.74" size="1.778" layer="95"/>
</segment>
</net>
<net name="D8" class="0">
<segment>
<pinref part="PH-DIR" gate="G$1" pin="5"/>
<wire x1="38.1" y1="58.42" x2="45.72" y2="58.42" width="0.1524" layer="91"/>
<label x="38.1" y="58.42" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="CON-AR-1" gate="G$1" pin="1"/>
<wire x1="-10.16" y1="96.52" x2="-10.16" y2="104.14" width="0.1524" layer="91"/>
<label x="-10.16" y="101.6" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="CON-AR-1" gate="G$1" pin="2"/>
<wire x1="-10.16" y1="81.28" x2="-10.16" y2="73.66" width="0.1524" layer="91"/>
<label x="-10.16" y="78.74" size="1.778" layer="95"/>
</segment>
</net>
<net name="D7" class="0">
<segment>
<pinref part="PH-DIR" gate="G$1" pin="6"/>
<wire x1="38.1" y1="55.88" x2="45.72" y2="55.88" width="0.1524" layer="91"/>
<label x="38.1" y="55.88" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="CON-AR-1" gate="G$1" pin="5"/>
<wire x1="-15.24" y1="96.52" x2="-15.24" y2="104.14" width="0.1524" layer="91"/>
<label x="-15.24" y="99.06" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="CON-AR-1" gate="G$1" pin="6"/>
<wire x1="-15.24" y1="81.28" x2="-15.24" y2="73.66" width="0.1524" layer="91"/>
<label x="-15.24" y="78.74" size="1.778" layer="95"/>
</segment>
</net>
<net name="D6" class="0">
<segment>
<pinref part="PH-DIR" gate="G$1" pin="7"/>
<wire x1="38.1" y1="53.34" x2="45.72" y2="53.34" width="0.1524" layer="91"/>
<label x="38.1" y="53.34" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="CON-AR-1" gate="G$1" pin="10"/>
<wire x1="-20.32" y1="81.28" x2="-20.32" y2="73.66" width="0.1524" layer="91"/>
<label x="-20.32" y="78.74" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="CON-AR-1" gate="G$1" pin="9"/>
<wire x1="-20.32" y1="96.52" x2="-20.32" y2="104.14" width="0.1524" layer="91"/>
<label x="-20.32" y="99.06" size="1.778" layer="95"/>
</segment>
</net>
<net name="M1-1" class="0">
<segment>
<pinref part="PH-ESQ" gate="G$1" pin="4"/>
<wire x1="-5.08" y1="60.96" x2="-12.7" y2="60.96" width="0.1524" layer="91"/>
<label x="-12.7" y="60.96" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="A=M1" gate="1" pin="1"/>
<wire x1="-40.64" y1="68.58" x2="-48.26" y2="68.58" width="0.1524" layer="91"/>
<label x="-48.26" y="68.58" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="A=M1" gate="1" pin="2"/>
<wire x1="-25.4" y1="68.58" x2="-17.78" y2="68.58" width="0.1524" layer="91"/>
<label x="-25.4" y="68.58" size="1.778" layer="95"/>
</segment>
</net>
<net name="M1-2" class="0">
<segment>
<pinref part="PH-ESQ" gate="G$1" pin="5"/>
<wire x1="-5.08" y1="58.42" x2="-12.7" y2="58.42" width="0.1524" layer="91"/>
<label x="-12.7" y="58.42" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="A=M1" gate="1" pin="6"/>
<wire x1="-25.4" y1="63.5" x2="-17.78" y2="63.5" width="0.1524" layer="91"/>
<label x="-25.4" y="63.5" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="A=M1" gate="1" pin="5"/>
<wire x1="-40.64" y1="63.5" x2="-48.26" y2="63.5" width="0.1524" layer="91"/>
<label x="-48.26" y="63.5" size="1.778" layer="95"/>
</segment>
</net>
<net name="M2-2" class="0">
<segment>
<pinref part="PH-ESQ" gate="G$1" pin="6"/>
<wire x1="-5.08" y1="55.88" x2="-12.7" y2="55.88" width="0.1524" layer="91"/>
<label x="-12.7" y="55.88" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="B=M2" gate="1" pin="5"/>
<wire x1="58.42" y1="63.5" x2="50.8" y2="63.5" width="0.1524" layer="91"/>
<label x="50.8" y="63.5" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="B=M2" gate="1" pin="6"/>
<wire x1="73.66" y1="63.5" x2="81.28" y2="63.5" width="0.1524" layer="91"/>
<label x="73.66" y="63.5" size="1.778" layer="95"/>
</segment>
</net>
<net name="M2-1" class="0">
<segment>
<pinref part="PH-ESQ" gate="G$1" pin="7"/>
<wire x1="-5.08" y1="53.34" x2="-12.7" y2="53.34" width="0.1524" layer="91"/>
<label x="-12.7" y="53.34" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="B=M2" gate="1" pin="1"/>
<wire x1="58.42" y1="68.58" x2="50.8" y2="68.58" width="0.1524" layer="91"/>
<label x="50.8" y="68.58" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="B=M2" gate="1" pin="2"/>
<wire x1="73.66" y1="68.58" x2="81.28" y2="68.58" width="0.1524" layer="91"/>
<label x="73.66" y="68.58" size="1.778" layer="95"/>
</segment>
</net>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
</eagle>
