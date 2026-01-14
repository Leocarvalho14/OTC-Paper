# 2022 Report.pdf (Text Extraction)

## Page 1

Monthly reportJanuary – December 2022
Issued by Shape with the support of MODEC
Monthly report
Prepared by Shape with the support of MODECDecember 2022

## Page 2

Monthly reportJanuary – December 2022
Breakdown of losses, $M USD, 2022 Jan - Nov48,1337,7826,6410,3511,14Total Potential LossesNon-Avoided LossesNon-avoided Addressable LossesNon-avoided Non-Addressable LossesPotential Avoided LossesConclusion of MV30 and MV31 PdM replication. Total of 249 new equipment, including new model for MV30 Siemens GTG.Concluded the elaboration of electric Generator prioritized algorithms based on FMEA and performed the basic replication to all GTG generators in the fleet.The two potential scaling cases in MV27 and MV30 identified by PdM tool on Nov 3rdand Oct 28th, respectively, are still under investigation.The scaling model's implementation is not complete due to the lack of sensor historical data. We are now working on the model’s infrastructure to ensure that new techniques could be developed. 
Highlights
Theoretical total loss if PdM was not being used. It is calculated as the sum of Potential Avoided Losses and Non-Avoided Losses.Sum of potential losses avoided by PdM (detection cases). These gains are predicted and are counted after a maintenance notification is issued.Sum of true losses as recorded by MODEC in Salesforce.Subset of Non-Avoided Losses that cannot be avoided by PdM, either by definition(e.g., offloading delays) or due to the lack of required sensing technology. This definition will be updated as situation changes.Subset of Non-Avoided Losses that could have been avoided by PdM(i.e., we have the required sensors installed to monitor the failure mode).Reasons for these failures include coverage gaps (equipment or failure modes for which we do not have a model yet), model failure (our existing models failed to detect the issue), or execution issues (appropriate mitigation action was either not recommended or not executed before the failure happened).
Total Potential Losses1Potential Avoided LossesNon-Avoided LossesNon-Addressable Non-Avoided LossesAddressable Non-Avoided Losses
MetricWhat the metric means
Lowlights
Losses, $M USD, 2022 Jan - Dec
18,334,858,316,2911,1426,64Non-Avoided Adressable  LossesNon-AvoidedNon-Addressable LossesNAMsDowntime
ML1ML2

## Page 3

Slide 2
ML1 Estava 9,68 alterei para 11,14
Melissa Lopes; 2023-01-09T19:00:32.529
ML2 Ainda sem os de dezembro
Melissa Lopes; 2023-01-09T19:06:52.180

## Page 4

Monthly reportJanuary – December 2022Worst case Potential Saving (USD)Short storyModelling approachNotification dateEquipment tagEquipmentVesselNo $500.000 The system detected abnormal temperature would lead to bearing damage and replacement.Machine learning2022-04-02MV29-CM-2210A-5SMV29-CM-2210A (MOTOR MAIN A)MV291 $500.000 The system detected abnormal axial displacement could lead to equipment misaligmentMachine learning2022-04-01MV30-1S-CBA-2120AMV30-CBA-2110A (VRU A)MV302 $1,700.750 The system detected that the lost of efiency in the heat exchanger can be caused by scaling depositMachine learning2022-05-15MV27-HZZ-1110A-2P /MV27-HZZ-1110B-2P/MV27-HZZ-1110C-2PMV27-HZZ1110-A/B/C (Crude Crude)MV273 $50.000 The system detected that abnormal temperature in the fuel nozzles that requires sensor replacementMachine learning2022-05-23MV24-GTG-4010C-8SMV24-GTG-4010A (GTG)MV244 $600.000 The system detected high vibration of the pump and electric motor DE bearings with signals of misalignmentKnowledge-based 2022-06-22MV26-PAT-1545A-5PMV26-PAT-1545A (SWIP A)MV265 $95.000 The system detected a oil level decreasing tendency on the last 6.6 days previous at the alarmKnowledge-based 2022-06-09MV24-PAT-1545C-5PMV24-PAT-1545C (SWIP C)MV246 $95.000The system detected a oil level decreasing tendency on the last 16.4 days previous at the alarmKnowledge-based 2022-07-11MV24-PAT-1545A-5PMV24-PAT-1545A (SWIP A)MV247 $200.000 The system detected a overheating on temperature sensors of  NDE Bearing that could lead to bearing damagesKnowledge-based 2022-07-26MV26-PBE-1525A-6P MV26-PBE-1525A (SRU A)MV268 $95.000 High temperature on one of three motor phases.Knowledge-based 2022-07-21MV24-CM-2430A-5SMV24-CM-2430A (MOTOR RE-INJECTION)MV249 $75.000 System detected incipient signals of sensor's abnormal readigns with under zero measurementsKnowledge-based2022-08-31MV26-CBA-2110A-1CMV26-CBA-2110A (VRU A)MV2610 $230.000 The system detected abnormal temperature would lead to bearing damage and replacement.Machine learning2022-09-17MV30-3S-TE-2413-60AMV30-CBA-2210A (MAIN B)MV3011 $150.000 The system detect a high vibration in the pump DE side that could damage the bearings Knowledge-based 2022-08-09MV27-PAT-1545C-8PMV27-PAT-1545C (SWIP C)MV2712 $1,694.000 System displayed an increase of dp on the hot sideMachine learning2022-08-15MV26-HZZ-1110A-3P / MV26-HZZ-1110B-3PMV26-HZZ-1110A/B (Crude Crude)MV2613 $1,619.000System displayed an increase of differential pressure on the hot sideMachine learning2022-09-01MV24-HZZ-1110A-3P / MV24-HZZ-1110B-3PMV24-HZZ-1110A/B (Crude Crude)MV2414 $ 1.272.790 System detected an abnormal vibration readingKnowledge-based2022-09-18TIT-2210C-23MV24-CBA-2210B-3SMV2415 $ 120,000 Crude Heater Sensor MalfunctioningMachine learning2022-10-25MV30-HBG-1120ACrude Crude Exchanger -A/B/CMV3016 $ 600,000Abnormal Motor Bearing High Vibration in SWLPKnowledge-based2022-10-02MV27-PM-4205A-MDMV27-PM-4205A (SWLP)MV2717 $ 150,000 Pump high bearing vibration and shaft displacement in SWIPKnowledge-based2022-10-24MV27-PAT-1545B-8PMV27-PAT-1545B (SWIP)MV2718 $ 600,000Pump Operation under Minimum Continous FlowKnowledge-based2022-11-21MV31-SRU-PBE-4205AMV31-PBE-4205A (SWLP)MV3119 $10.346,54Total saving (KUSD)
Retroactive casesSummary of successful cases
ML1

## Page 5

Slide 3
ML1 Adicionar cases novos
Melissa Lopes; 2023-01-10T18:49:25.379

## Page 6

Monthly reportJanuary – December 2022
Issued by Shape with the support of MODEC
CASE 1 | MV29 - Motor NDE Bearing temperature increaseNumber of operationsNumber of variablesEQUIPMENT | TAGVESSEL522MV29-CM-2210A-5SMV29ACTION STATUS MODELLING APPROACHNOTIFICATION DATECompletedMachine Learning2022-02-04EVENT DESCRIPTIONDuring the MV29 rotating equipment condition monitoring routine in conjunction with Shape, it was identified that the temperature ofthe NDE radial bearing (TI-2210A-74) of the Main Compressor A train 1 electric motor showed a marked increase in the last 60 days fromthe values previously presented (92°C) and is currently operating at the 62°C range.SHAPE’S APPLICATION
SPECIALIST’S RECOMMENDATIONRecommendations: 1. Check the integrity of the sensor regarding the condition of the wirings and check the calibration of the TI-2210A-74 and TI-2210A-73 instruments2. Visually check the oil flow and make a photographic record of the SIGHT GLASS BP-237-07 and BP-237-08 from the Lube Oil return line from the engine to the Lubrication Unit.3. Visually check and photograph the RO 2210A-52 and RO-2210A-58 for possible oil flow obstructionOutcomes: It was confirmed that the actions requested by notes were performed and as a result of the maintenance reports, we can conclude that the signal presented by the sensor was a spurious reading due to lose wiring in the terminal block (A9 and B9) inside the 5S-IJB-2210A-73 junction box, which after being retightened, returned to read similar to its peer instrument (MV29-TE-2210A-73-5S ), as expected.
POTENTIAL SAVING ASSESSMENT$ 500.000$ 20.000WORST SCENARIOBEST SCENARIOMaintenance type: EmergencyMaintenance type: PlannedMaintenance scope: Replace 1ststage rotor due damage caused by lack of protection or unplanned machine shutdown.Estimated Potential cost considered is the “replace 1ststage rotor” of VRU Compressor 1ststage at Money Counter. It was not considered any downtime or flare costMaintenance scope: Sensor’s evaluation and potential replacementDowntime impact: Low riskDowntime impact: No impactEquipment unavailability: YesEquipment unavailability: Yes

## Page 7

Monthly reportJanuary – December 2022
Issued by Shape with the support of MODEC
CASE 2 | MV30 – VRU Compressor – Axial displacement monitoringACTION STATUSMODELLING APPROACHNOTIFICATION DATECompletedKnowledge-based2022-05-23EVENT DESCRIPTIONThe ZI2175-82 sensor showed a gradual increase, and its pair (ZI2175-81) was not keeping up.This type of behavior represents a non-conformity that can be fixation or calibration and needs to be inspected.Number of operationsNumber of variablesEQUIPMENT | TAGVESSEL625MV30-CBA-2110BMV30
SPECIALIST’S RECOMMENDATIONThe problem is mapped and tracked; this behavior is usually associated with fixation or calibration and needs to be inspected. In this case, the compressor must be stopped to check the instrumentation as the first approach. This activity needs at least one working day, but since VRU A is unavailable at this moment, maintenance stops are not being made on VRU B. The monitoring of this variable is being closely performed by MdB team.POTENTIAL SAVING ASSESSMENTZoom in to see it larger
$ 500.000$ 20.000WORST SCENARIOBEST SCENARIOMaintenance type:EmergencyMaintenance type:PlannedMaintenance scope:Replace 1ststage rotor due damage caused by lack of protection or unplanned machine shutdown.Estimated Potential cost considered is the “replace motor” of Main A Engine at Money Counter. It was not considered any downtime or flare cost.Maintenance scope:Replace instrumentationDowntime impact: Low riskDowntime impact: No impactEquipment unavailability:YesEquipment unavailability:Yes


## Page 8

Monthly reportJanuary – December 2022
Issued by Shape with the support of MODEC
CASE 3 | Scaling deposits in the crude crude exchangersNumber of operationsNumber of variablesEQUIPMENT | TAGVESSEL94MV27-HZZ-1110A/B/CMV27ACTION STATUS MODELLING APPROACHNOTIFICATION DATECompletedMachine Learning2022-10-05EVENT DESCRIPTIONThe system detected a performance loss in the Crude/crude exchanger (HZZ1110-A/B/C) caused by scaling deposit. This behavior wasobserved through the pressure drop increase. The system monitors the differential pressure tags PDI-1110A/B/C-12 and PDI-1110A/B/C-05.SHAPE’S APPLICATION
SPECIALIST’S RECOMMENDATIONOperations and Engineering developed a cost-effective plan to partially renew equipment performance by flushing with warm fresh water (considering that solids would be halite). Operations promptly took action and gave feedback on improved hydraulics. Flush was performed for approximately 24hrs at Crude-Crude A (HZZ1110-A), and the pressure drop normalization was observed. It also was planned to perform the flush at exchangers B (HZZ1110-B) and C (HZZ1110-B).
POTENTIAL SAVING ASSESSMENT$ 1.700.750$ 120.000WORST SCENARIOBEST SCENARIOMaintenance type: EmergencyMaintenance type: PlannedMaintenance scope: Well shutdown for scale cleaning (3 days)In addition to the previous scenario, as severe scaling conditions evolve, the heat exchanger can become blocked and therefore inoperable due to back pressure. Maintenance scope: Replacement of heat exchanger A/BFlushing process is not effective leadingto corrosion of the heat exchanger whichcan often be hidden by the scaling layeritself. This shortens the working life of the heat exchanger resulting in its replacement in a long term.Downtime impact: High riskDowntime impact: No impactEquipment unavailability: YesEquipment unavailability: No


## Page 9

Monthly reportJanuary – December 2022
Issued by Shape with the support of MODEC
CASE 4 | MV24 - GTG C Combustion – GTG Spread MonitoringNumber of operationsNumber of variablesEQUIPMENT | TAGVESSEL813MV24-GTG-4010CMV24ACTION STATUSMODELLING APPROACHNOTIFICATION DATECompletedKnowledge-based2022-05-23EVENT DESCRIPTIONThe sensor TE-8043A [I_T48_T48A_A] signal is showing erratic behavior. The sensor trend is oscillating, with higher standard deviation from normal operational behavior. It could be caused by an issue in the acquisition loop or the sensor itself.SHAPE’S APPLICATION
SPECIALIST’S RECOMMENDATIONThe sensor inspection of TE-8043 A [I_T48_T48A_A] was requested to check the acquisition loop (connection, wiring, and cabling), the sensor integrity and its installation. If the failure persists, the sensor replacement will be performed at the first available opportunity in the preventive maintenance schedule.POTENTIAL SAVING ASSESSMENTZoom in to see it larger
$ 50.000$ 50.000WORST SCENARIOBEST SCENARIOMaintenance type:EmergencyMaintenance type:PlannedMaintenance scope:Replace instrumentation.Estimated Potential cost considered is the cost of “replace instrumentation of GTG Combustion” at Money Counter.Maintenance scope:Replace instrumentationDowntime impact:No impact.Downtime impact:No impactEquipment unavailability:YesEquipment unavailability:Yes


## Page 10

Monthly reportJanuary – December 2022
Issued by Shape with the support of MODEC
CASE 5 | Sea Water Injection Pump presenting signs of misalignmentNumber of operationsNumber of variablesEQUIPMENT | TAGVESSEL1124MV26-PAT-1545A-5PMV26ACTION STATUS MODELLING APPROACHNOTIFICATION DATECompletedKnowledge-based2022-07-06EVENT DESCRIPTIONAfter pump mechanical intervention (Bundle replacement) on June / 2022, it was identified a high vibration of the pump and electric motor DE bearings with signals of misalignment. Vibration, temperature, lube oil system, and process parameters were checked throughSystem 1 and PI trend. They were normal conditions, except for pump and electric motor DE bearing vibration readings (Pump: VXE1545B-01 and VYE1545B-02 – Electric motor: VI-1545A-13 and VI-1545A-14), after pump mechanical intervention (bundle replacement).The vibration data (spectrum, orbit, and polar) readings were checked to identify any harmonics responsible for the increase in vibration. The 1st and 2nd harmonics have increased, and the reason may be misalignment and damaged coupling blade. SHAPE’S APPLICATION
SPECIALIST’S RECOMMENDATIONRecommendations:1. Check pump alignment; DBFF, coupling ́s shims conditions / quantity / thickness, and screws torque; 2. Electric motor ́s shims conditions / quantity / thickness. Outcomes: After Tier 2 recommendations were done, the pump vibration data are in normal conditions, and the vibration amplitude peaks are compatible between DE and NDE bearings POTENTIAL SAVING ASSESSMENTZoom in to see it larger
$ 600.000$ 20.000WORST SCENARIOBEST SCENARIOMaintenance type: EmergencyMaintenance type: PlannedMaintenance scope: Replacement of bearing and pump internal parts due the damage caused by high vibration.Estimated Potential cost considered is the “replace bundle” of SWIP at Money Counter.Maintenance scope: Pump Alignment, coupling, shims, and screwstorque inspection. Downtime impact: Low riskDowntime impact: No impactEquipment unavailability: YesEquipment unavailability: Yes

## Page 11

Monthly reportJanuary – December 2022
Issued by Shape with the support of MODEC
CASE 6 | Sea Water Injection Pump C– Lube Oil LeakageACTION STATUS MODELLING APPROACHNOTIFICATION DATEOngoingKnowledge-based2022-05-03EVENT DESCRIPTIONIt was identified during the monitoring routine in PdM a decreasing tendency in the lube oil in the lube oil reservoir level transmitter (LIT-1546C-01). There is a notification (10670188)to mitigate this leakage that dates to 01/04/2022, generated by the production team, but theevent persists.As we can see in the level transmitter (LIT-1546C-01) trend below, there is a decreasing tendency that is mitigated byrefueling the reservoir when it reaches a level below 60%.SHAPE’S APPLICATION
SPECIALIST’S RECOMMENDATIONThe following equipment must be checked for oil leakage:•Flexible hoses;•Expansion joints;•Reservoir;•Lube oil coolers (HZZ-1548A & HZZ-1548B).POTENTIAL SAVING ASSESSMENT$ 95.000$ 2.520WORST SCENARIOBEST SCENARIOMaintenance type: EmergencyMaintenance type: PlannedMaintenance scope: Huge oil  leakage through the reservoir that requires corrective actions such as welding procedures and non-destructive tests.Estimated Potential cost considered is the “replace other parts” of Main A Engine at Money Counter.Maintenance scope: Check lube oil system for possible leakage identification and replacement of minor components (flexible hoses,  connections, small valves, gaskets, etc) if necessary.Downtime impact: Medium riskDowntime impact: No impactEquipment unavailability: Yes, 30 daysEquipment unavailability: Yes, 1 day
Zoom in to see it larger
Number of operationsNumber of variablesEQUIPMENT | TAGVESSEL69MV24-PAT-1545C-5PMV24

## Page 12

Monthly reportJanuary – December 2022
Issued by Shape with the support of MODEC
CASE 7 | Sea Water Injection Pump A – Lube Oil LeakageACTION STATUS MODELLING APPROACHNOTIFICATION DATEOngoingKnowledge-based2022-07-11EVENT DESCRIPTIONIt was identified during the monitoring routine in PdM a decreasing tendency in the lube oil in the lube oil reservoir level transmitter (LIT-1545A-01) decreasing tendency since 29/01/2022. It was analyzed the history of the oil level sensor and it was found that always afterrefueling the sensor showed a decrease in the level. Signs of possible leak or sensor failure.SHAPE’S APPLICATION
SPECIALIST’S RECOMMENDATIONThe following equipment must be checked for oil leakage:•Flexible hoses;•Expansion joints;•Reservoir;•Lube oil coolers (HZZ-1548A & HZZ-1548B).POTENTIAL SAVING ASSESSMENT$ 95.000$ 3.000WORST SCENARIOBEST SCENARIOMaintenance type: EmergencyMaintenance type: PlannedMaintenance scope: Huge oil  leakage through the reservoir that requires corrective actions such as welding procedures and non-destructive tests.Estimated Potential cost considered is the “replace other parts” of Main A Engine at Money Counter.Maintenance scope: Check lube oil system for possible leakage identification and replacement of minor components (flexible hoses,  connections, small valves, gaskets, etc) if necessary.Downtime impact: Medium  riskDowntime impact: No impactEquipment unavailability: YesEquipment unavailability: Yes
Zoom in to see it larger
As we can see in the level transmitter (LIT-1546A-01) trend below, there is a decreasing tendency that is mitigated by refiling the reservoir when it reaches a level below 60% 
Number of operationsNumber of variablesEQUIPMENT | TAGVESSEL69MV24-PAT-1545A-5PMV24

## Page 13

Monthly reportJanuary – December 2022
Issued by Shape with the support of MODEC
CASE 8 | Motor NDE Bearing temperature increaseACTION STATUS MODELLING APPROACHNOTIFICATION DATECompletedKnowledge-based2022-07-26EVENT DESCRIPTIONDuring last CIP Event (July / 2022), it was identified an increasing of NDE bearing temperature (above pre- alarm >70oC), while SRU A/B pump flow rate have decreased to clean filter, the SRU Pump B flow rate was approximately 780 m3/h, and SRU Pump A flow rate wasapproximately 450 m3/h. SRU A/B flow rate is 1200 m3/h for each pump during normal operating conditions. Bearing temperature alarm / trip set point are 95 / 105oC. SHAPE’S APPLICATION
SPECIALIST’S RECOMMENDATIONAdjust operating point from 852 to 1332 m3/h so that the pump operates in the preferred operation region. POTENTIAL SAVING ASSESSMENT$ 200.000$ 20.000WORST SCENARIOBEST SCENARIOMaintenance type: EmergencyMaintenance type: PlannedMaintenance scope: Replacement of bearings due damage caused by lack of protection or unplanned machine shutdown.Estimated Potential cost considered is the “repair onshore” of SWIP at Money Counter. Maintenance scope: Process Adjustment Downtime impact: Low riskDowntime impact: No impactEquipment unavailability: Yes, 30 daysEquipment unavailability: Yes, 1 day
Number of operationsNumber of variablesEQUIPMENT | TAGVESSEL1124MV26-PBE-1525A-6P MV26

## Page 14

Monthly reportJanuary – December 2022
Issued by Shape with the support of MODEC
CASE 9 | Electric Motor Winding Temperature Transmitter MalfunctionACTION STATUS MODELLING APPROACHNOTIFICATION DATEOngoingKnowledge-based2022-07-21EVENT DESCRIPTIONIt was identified during the monitoring routine in PDM a malfunction in the electric motor winding temperature transmitter (TIT-2430A-54). It was identified as displayed in the trend below. The electric motor temperature transmitter (TIT-2430A-54) readings show a spurious signal that may cause a false trip in the equipment. SHAPE’S APPLICATION
SPECIALIST’S RECOMMENDATION1. Perform a physical inspection on the sensor loop, looking for the source of noise, check junction box and perform the change over to spare temperature transmitter 2. Inhibit the sensor to avoid trips in the machine until there is an opportunity to perform the raised work order. POTENTIAL SAVING ASSESSMENT$ 95.000$ 95.000WORST SCENARIOBEST SCENARIOMaintenance type: PlannedMaintenance type: PlannedMaintenance scope: Check electric motor winding temperature transmitter for connection problems, perform a change over to spare temperature transmitter.Estimated Potential cost considered is the “replace instrumentation” of Main B Engine at Money CounterMaintenance scope: Check electric motor winding temperature transmitter for connection problems, perform a change over to spare temperature transmitter.Downtime impact: Medium riskDowntime impact: Low riskEquipment unavailability: Yes. Equipment unavailability: Yes. 
Zoom in to see it larger
Number of operationsNumber of variablesEQUIPMENT | TAGVESSEL1333MV24-CM-2430A-5SMV24

## Page 15

Monthly reportJanuary – December 2022
Issued by Shape with the support of MODEC
CASE 10 | Compressor bearing temperature malfunctionACTION STATUS MODELLING APPROACHNOTIFICATION DATEOngoingKnowledge-based2022-08-31EVENT DESCRIPTIONGearbox bearing temperature transmitter (TIT-2110A-24) readings of VRU have been showing a high difference than other temperaturetransmitters (TIT-2110A-22, TIT-2110A-23, and TIT-2110A-25). Once PdM tool alarmed, the specialist checked the case and confirmed thatthis behavior may represent sensor's malfunction.SHAPE’S APPLICATION
SPECIALIST’S RECOMMENDATIONThe temperature transmitter (TIT-2110A-24) must be checked and calibrated; the replacement must be done if calibration is unavailable ornot properly well; instruments´ piping must be inspected and/or cleaned.POTENTIAL SAVING ASSESSMENT$ 75.000$ 20.000WORST SCENARIOBEST SCENARIOMaintenance type: EmergencyMaintenance type: PlannedMaintenance scope: Replacement of VRU bearings due gearbox damage caused by lack of protection orunplanned machine shutdown.Estimated Potential cost considered is the “replace bearings” of VRU Engine of MV26 at Money Counter.Maintenance scope: Sensor’s evaluation and potential replacementDowntime impact: No impact.Downtime impact: No impactEquipment unavailability: YesEquipment unavailability: No
Zoom in to see it larger
Number of operationsNumber of variablesEQUIPMENT | TAGVESSEL1418MV26-CBA-2110A-1CMV26

## Page 16

Monthly reportJanuary – December 2022
Issued by Shape with the support of MODEC
CASE 11 | Compressor bearing temperature malfunction
ACTION STATUS MODELLING APPROACHNOTIFICATION DATEOngoingMachine learning2022-09-17EVENT DESCRIPTIONCompressor bearing temperature sensor (MV30-3S-TE-2413-60A) readings have been showing a high difference than other temperature sensors. Once the PdM tool alarmed, the specialist checked the case and confirmed that this behavior may represent the sensor's malfunction, since the bearing vibrations are all normal and the temperature values from this speciﬁc sensor   are varying a lot over time during the equipment’s normal operation condition.SHAPE’S APPLICATION
SPECIALIST’S RECOMMENDATIONAfter receiving the notification from Shape, the specialist evaluated it with the onboard team and increased the priority of a maintenance note that was open for this sensor (MV30-3S-TE-2413-60A) to check general conditions instrument and loop: connections, tightness of terminals and control panel terminals, and communication loop. If necessary, evaluate the replacement's opportunity.POTENTIAL SAVING ASSESSMENT$ 230.000$ 20.000WORST SCENARIOBEST SCENARIOMaintenance type: EmergencyMaintenance type: PlannedMaintenance scope: Replacement of bearings due damage caused by lack of protection or unplanned machine shutdown.Estimated Potential cost considered is the “replace bearings” of Main A Compressor at Money Counter.Maintenance scope: Sensor’s evaluation and potential replacementDowntime impact: Medium riskDowntime impact: No impactEquipment unavailability: YesEquipment unavailability: No
Number of operationsNumber of variablesEQUIPMENT | TAGVESSEL414MV30-3S-TE-2413-60AMV30

## Page 17

Monthly reportJanuary – December 2022
Issued by Shape with the support of MODEC
CASE 12 | Abnormal radial bearing vibration in pump DE sideACTION STATUS MODELLING APPROACHNOTIFICATION DATEOngoingKnowledge-based2022-09-08EVENT DESCRIPTIONThe vibration of the pump bearing on the DE side of SWIP (MV27-VI-1545C-02-5P) increased significantly reaching a plateau of 60-micron(Hi = 60 / HiHi = 90 microns). Once the PdM tool alarmed, the oscillations above the expected limit for this vibration (MV27-VI-1545C-02-5P) were identified as consistent with misalignment characteristics and coupling issues.SHAPE’S APPLICATION
Zoom in to see it largerSPECIALIST’S RECOMMENDATIONCheck coupling (blades, gap, distance) of main pump,  alignment and check coupling of the pump.POTENTIAL SAVING ASSESSMENT$ 150.000$ 20.000WORST SCENARIOBEST SCENARIOMaintenance type:EmergencyMaintenance type:PlannedMaintenance scope:Replacement of bearing and coupling due the damage to the thrust bearings caused by high vibration during long period.Estimated Potential cost considered is the “replace coupling and mechanical seal” of  SWIP at Money Counter.Maintenance scope:Pump alignmentDowntime impact:Medium risk Downtime impact:No impactEquipment unavailability:YesEquipment unavailability:No
Number of operationsNumber of variablesEQUIPMENT | TAGVESSEL1124MV27-PAT-1545C-8PMV27

## Page 18

Monthly reportJanuary – December 2022
Issued by Shape with the support of MODEC
CASE 13 | Scaling deposits in the exchangersACTION STATUS MODELLING APPROACHNOTIFICATION DATECompletedMachine learning2022-08-15EVENT DESCRIPTIONDuring the process of reviewing the MV26 monitoring models on August/22, the specialist detected initial signs of scaling. Thus, it wasattested that the Crude Crude hot side (PDI-1110A-12) Dp is above the design – 80 kPa vs the 65.7 kPa (design). The dP of Crude Crude coldside(PDI-1110A-05) has been showing an upward trend for two months (it rose from 70 to 115 kPa). Crude Heater dP has been showing thesame trend (in two months it rose from 80 to 120 kPa).SHAPE’S APPLICATION
SPECIALIST’S RECOMMENDATIONThe specialist requested an evaluation of Crude Crude A/B backflushing with fresh water – hot and cold oil sides – during operation in normal production. In order to partially renew equipment performance, the specialist recommended backflushing with fresh water each equipment for 2 days straight. The equipment should be isolated and have its flow diverted to the remaining Crude Crude. POTENTIAL SAVING ASSESSMENT
$ 1.694.000$ 120.000WORST SCENARIOBEST SCENARIOMaintenance type: EmergencyMaintenance type: PlannedMaintenance scope: Well shut down for scale cleaning resulting in 3 days of 100% downtime. In addition to the previous scenario, as severe scaling conditions evolve, the heat exchanger can become blocked and therefore inoperable due to back pressure. Maintenance scope: Replacement of heat exchanger A/BIn case the backflushing process is noteffective leading scaling can not beremoved offshore and a new plate pack is required to renew performance. Downtime impact: High riskDowntime impact: No impactEquipment unavailability: YesEquipment unavailability: Yes
Number of operationsNumber of variablesEQUIPMENT | TAGVESSEL94MV26-HZZ-1110A-3P / MV26-HZZ-1110B-3PMV26

## Page 19

Monthly reportJanuary – December 2022
Issued by Shape with the support of MODEC
CASE 14 | Carbonate deposits in the crude crude exchangersACTION STATUS MODELLING APPROACHNOTIFICATION DATECompletedMachine learning2022-09-01EVENT DESCRIPTIONWhile reviewing the MV24 scaling models, we noticed that Crude/Crude is performing very poorly on the hot side. The cold side dP(MV24_PDI-1110A-12/MV24_PDI-1110B-12) begins a downward trajectory that isn't followed by the hot side dP (MV24_PDI-1110A-05/MV24_PDI-1110A-05). At full flow, the cold side would have dP of 200 kPa, and the hot side should proportionally be around 50% of thecold side. Instead, the hot side reaches 65-70 when the cold side is only 70kPa.SHAPE’S APPLICATION
Zoom in to see it largerSPECIALIST’S RECOMMENDATIONThe specialist requested evaluation of Crude Crude A/B backflushing with fresh water – hot and cold oil sides – during operation in normal production. The analysis of solids found in the pump´s spool indicated carbonate. Based on MV26 August event, in order to partially renew equipment performance, the specialist recommended backflushing with fresh water each equipment for 2 days straight. The equipment should be isolated and have its flow diverted to the remaining Crude Crude. POTENTIAL SAVING ASSESSMENT$ 1.619.000$ 120.000WORST SCENARIOBEST SCENARIOMaintenance type: EmergencyMaintenance type: PlannedMaintenance scope: Well shut down for scale cleaning resulting in 3 days of 100% downtime. In addition to the previous scenario, as severe scaling conditions evolve, the heat exchanger can become blocked and therefore inoperable due to back pressure. Maintenance scope: Replacement of heat exchanger A/BIn case the backflushing process is noteffective leading scaling can not beremoved offshore and a new plate pack is required to renew performance. Downtime impact: High riskDowntime impact: No impactEquipment unavailability: YesEquipment unavailability: Yes
Number of operationsNumber of variablesEQUIPMENT | TAGVESSEL94MV24-HZZ-1110A-3P / MV24-HZZ-1110B-3PMV24
MABC1
MABC2

## Page 20

Slide 17
MABC1 [@Julianna Braga]Quando iniciou a queda do delta P do lado frio… vamos colocar 
datas
Michele Aguiar Buccazio Câmara; 2022-11-09T13:26:00.082
MABC2 Alterei o status para ongoing
Michele Aguiar Buccazio Câmara; 2022-11-09T13:26:15.659

## Page 21

Monthly reportJanuary – December 2022
Issued by Shape with the support of MODEC
CASE 15 | Compressor trip caused overload in the redundancyACTION STATUS MODELLING APPROACHNOTIFICATION DATEOngoingKnowledge-based2022-09-18EVENT DESCRIPTIONAfter a trip in Main A3 Compressor (MV24-CBA-2210C-3S) on August 17th, the Vibration transmitters (MV24-VE-2210B-13-3S/MV24-VE-2210B-14-3S) readings on DE side showed an elevated value with an increasing behavior reaching alarm limits. The study being carried bythe engineers investigated that the trip in the Main A3 compressor abruptly increased the load in the Main A2 Compressor.SHAPE’S APPLICATION
SPECIALIST’S RECOMMENDATION1. Perform a change over from Main A2 to Main A3;2. Inspect Main A2 coupling for possible damage on flexible blades.3. Check possible shaft misalignment after equipment shutdown. If possible, immediately after machine stoppage (hot alignmentcheck)POTENTIAL SAVING ASSESSMENT$ 1.272.690 $ 100.000WORST SCENARIOBEST SCENARIOMaintenance type: EmergencyMaintenance type: PlannedMaintenance scope: Replacement of the compressor and its internal components due to coupling failure. Estimated Potential cost considered is the “replace compressor bundle” of Main A Compressor at Money Counter.Maintenance scope: Blade coupling replacement and equipment alignmentDowntime impact: Medium risk.Downtime impact: No impactEquipment unavailability: Yes.Equipment unavailability: No impact
Zoom in to see it larger
Number of operationsNumber of variablesEQUIPMENT | TAGVESSEL1124MV24-CBA-2210B-3SMV24
JB1
MABC2

## Page 22

Slide 18
JB1 Felipe dividiu que a nova metodologia não chegou ainda na parte de 
compressores. Mas a ordem de grandeza para essa troca faz sentido para ele de 
acordo com o material que está sendo estudado no momento
Julianna Braga; 2022-10-28T17:18:52.548
MABC2 Tem risco de downtime?
Michele Aguiar Buccazio Câmara; 2022-11-09T13:28:01.411
JB2 0 Tem sim 
Julianna Braga; 2022-11-09T13:41:10.666
JB2 1 Será que não é a boa trocar esse production impact pra downtime risk?
Julianna Braga; 2022-11-09T13:41:36.777
MABC2 2 Acho que sim….
Michele Aguiar Buccazio Câmara; 2022-11-11T13:24:12.548
MABC2 3 E caso haja risco, informar de quantos dias
Michele Aguiar Buccazio Câmara; 2022-11-11T13:24:30.055
JB2 4 Não temos esse detalhamento ainda nessa metodologia infelizmente 
Julianna Braga; 2022-11-11T13:38:32.582
JB2 5 Consigo pegar o que está sendo considerado como Money Counter mas isso não 
sei se é tão direto assim
Julianna Braga; 2022-11-11T13:39:01.363

## Page 23

Monthly reportJanuary – December 2022
Issued by Shape with the support of MODEC
CASE 15 | Predictive Diagnose Avoid Major damage in the CompressorEQUIPMENT | TAGVESSELMV24-CBA-2210B-2SMV24ACTION STATUS MODELLING APPROACHNOTIFICATION DATEOngoingKnowledge-based2022-09-18EVENT DESCRIPTIONAfter a trip in Main A3 Compressor (MV24-CBA-2210C-3S) on August 17th, the Vibration on DE (Drive-End) side of the Main A2 Compressor (MV24-CBA-2210C-2S) showed an elevated value with an increasing behavior reaching PdM tool alarm limits. The PdM tool was able to capture an upward trend withthe vibration level still far from the machine alarm. The coupling damage diagnose was confirmed after an field inspection. The PdM tool supported theearlier awareness about the condition deviation, that could lead to severe damage in the compressor.SHAPE’S APPLICATION
SPECIALIST’S RECOMMENDATION1. Perform a change over from Main A2 to Main A3;2. Inspect Main A2 coupling for possible damage on flexible blades.3. Check possible shaft misalignment after equipment shutdown. If possible, immediately after machine stoppage (hot alignment check)POTENTIAL SAVING ASSESSMENT$ 1.272.690 $ 100.000WORST SCENARIOBEST SCENARIOMaintenance type: EmergencyMaintenance type: PlannedMaintenance scope: Replacement of the compressor and its internal components due to coupling failure. Estimated Potential cost considered is the “replace compressor bundle” of Main A Compressor at Money Counter.Maintenance scope: Blade coupling replacement and equipment alignmentDowntime impact: Medium risk.Downtime impact: No impactEquipment unavailability: Yes.Equipment unavailability: No impact
Zoom in to see it larger
Despite the relative simple premise of the pre-alarm’s algorithms, it’s an operational challenge to manage all the 1.860 pre-alarmsalgorithms applied to rotating equipment’s bearings, disregards the setpoints adjustments, alarms acknowledgments and support fordecision making. It is humanly impossible to monitor all data belonging to a system of equipment.The SHAPE’s PdM tool help to manage all the points presented above, extending the functionality of a traditional PIMS (PlantInformation Management System) solution, allowing a lean condition monitoring team to perform surveillance over a large amount ofequipment’s."

## Page 24

Monthly reportJanuary – November 2022
Issued by Shape with the support of MODEC
CASE 16 | Crude Heater Sensor MalfunctioningACTION STATUS MODELLING APPROACHNOTIFICATION DATECompletedMachine learning2022-10-25EVENT DESCRIPTIONDuring scaling modeling of new vessels, an abnormal behavior was detected on the differential pressure sensor of the crude heater’scrude oil side (PDI-1103-03). This tag is represented by the orange trend, below. The measured PDI didn’t match the expected flowrate. Asshown below, this problem was fixed with a sensor calibration, indicated by a great pressure drop with a steady flowrate in midnovember.SHAPE’S APPLICATION
SPECIALIST’S RECOMMENDATIONCheck sensor's connections, calibration, and the instrument itself. The instrument was back running again with calibration.POTENTIAL SAVING ASSESSMENT$ 120.000$ 20.000WORST SCENARIOBEST SCENARIOMaintenance type: EmergencyMaintenance type: PlannedMaintenance scope:Replacement of crude-crude heater due damage caused by lack of protection orunplanned machine shutdown.The cost impact estimated is the average price of a new equipment according to Modec.Maintenance scope: Sensor’s evaluation and potential replacementDowntime impact: No impactDowntime impact: No impact.Equipment unavailability: Yes.Equipment unavailability: Yes. 
Zoom in to see it larger
This abnormality is related to an instrument miscalibration
Number of operationsNumber of variablesEQUIPMENT | TAGVESSEL95MV30-HBG-1120AMV30

## Page 25

Monthly reportJanuary – December 2022
Issued by Shape with the support of MODEC
CASE 17 | Abnormal Motor Bearing High Vibration in SWLPACTION STATUS MODELLING APPROACHNOTIFICATION DATENot startedKnowledge-based2022-10-02EVENT DESCRIPTIONThe PdM tool generated an event of high vibration on both motor’s bearings, reaching values above the Trip limit without stopping the machine (possible malfunction of the protection system), the pump's bearing box also presented this condition. After the event initialinvestigation observed that this increase on bearing vibration began after the motors current decreased and reached the lowest value since the MV27 commissioning. Seven (7) hours after pump-motor system started the discharge pressure decreased and reached the lowest value since the MV27 commissioning, reaching values close to zero, that indicates a possible obstruction on pumps suction.SHAPE’S APPLICATION
SPECIALIST’S RECOMMENDATIONIt's recommended to keep the equipment out of operation, aiming to avoid further damages. Please, inspect the SWLP A and perform the recommendation of the guide pads replacement presented at the maintenance note: 10348867.POTENTIAL SAVING ASSESSMENT$ 600.000 $ 50.000WORST SCENARIOBEST SCENARIOMaintenance type: EmergencyMaintenance type: PlannedMaintenance scope: Replacement of the bearings and pump internal parts due the damage caused by marine life blocking the filter upstream the SWLP. Estimated Potential cost considered is the “replace bundle” of SWIP at Money CounterMaintenance scope: Change the rubber expansion joint.Downtime impact: No impactDowntime impact: No impactEquipment unavailability: Yes.Equipment unavailability: Yes.
Zoom in to see it larger
Number of operationsNumber of variablesEQUIPMENT | TAGVESSEL1124MV27-PM-4205A-MDMV27

## Page 26

Monthly reportJanuary – December 2022
Issued by Shape with the support of MODEC
CASE 18 | Pump high bearing vibration and shaft displacement in SWIPACTION STATUS MODELLING APPROACHNOTIFICATION DATEOngoingKnowledge-based2022-10-24EVENT DESCRIPTIONAfter MV27-PAT-1545B (SWIP) start-up it was observed an increase of bearing vibration and shaft axial displacement. The bearingvibration increased 10 micron and reached pre-alarm value, 60 micron (MV27_VI-1545B-01.PV). The axial displacement went from 130micron to 300 micron.SHAPE’S APPLICATION
SPECIALIST’S RECOMMENDATIONIt's recommended to inspect the axial displacement sensors - MV27-ZE-1545B-17-8P and MV27-ZE-1545B-18-8P - and its facilities (connections, cables, Junction box and its installation device). For the bearing vibration: inspect the main lube oil pump and its coupling.POTENTIAL SAVING ASSESSMENT$ 150.000 $ 20.000WORST SCENARIOBEST SCENARIOMaintenance type: EmergencyMaintenance type: PlannedMaintenance scope: Replacement of bearing and coupling due the damage to the thrust bearings caused by high vibration during long period.Estimated Potential cost considered is the “replace coupling and mechanical seal” of MV27 of SWIP at Money CounterMaintenance scope: Check the axial displacement sensors loop and Lube Oil Pump condition.Downtime impact: No impact.Downtime impact: No impact.Equipment unavailability: Yes.Equipment unavailability: No.
Zoom in to see it larger
Number of operationsNumber of variablesEQUIPMENT | TAGVESSEL1936MV27-PAT-1545B-8PMV27

## Page 27

Monthly reportJanuary – December 2022
Issued by Shape with the support of MODEC
CASE 19 | Pump Operation under Minimum Continous FlowACTION STATUS MODELLING APPROACHNOTIFICATION DATECompletedKnowledge-based2022-11-21EVENT DESCRIPTIONPdm model alarmed when Sea Water lifting pump (SWLP) started to operate below the allowable flow region as it can be seen at blueline at the following figure. Besides that, another Variable was observed before this event as filter differential pressure also increased.SHAPE’S APPLICATION
SPECIALIST’S RECOMMENDATIONThe engineer made contact with the team onboard and after the pump inspection they concluded that marine life was the cause of the pumps discharge obstruction. This happened due to some loose bolts on pump suction flange.POTENTIAL SAVING ASSESSMENT$ 600.000 $ 20.000WORST SCENARIOBEST SCENARIOMaintenance type: EmergencyMaintenance type: PlannedMaintenance scope: Replacement of the bearings and pump internal parts due the damage caused by marine life blocking the filter upstream the SWLP. Estimated Potential cost considered is the “replace bundle” of SWIP at Money Counter Maintenance scope: Cleaning of the pump suction line and tighten the suction flange bolts.Downtime impact: No impactDowntime impact: No impactEquipment unavailability: Yes.Equipment unavailability: Yes.
Zoom in to see it larger
Number of operationsNumber of variablesEQUIPMENT | TAGVESSEL510MV31-SRU-PBE-4205AMV31

## Page 28

Monthly reportJanuary – December 2022
Issued by Shape with the support of MODEC
CASE 20 | Temperature abnormal instrument readingACTION STATUS MODELLING APPROACHNOTIFICATION DATEOngoingKnowledge-based2022-10-31EVENT DESCRIPTIONAn PDM alarm identified that the electric motor´s winding temperature transmitters (TIT-2110A-12) have shown unstable readings. Thissensor started to show an increasing tendency that was evaluated by the specialists.SHAPE’S APPLICATION
SPECIALIST’S RECOMMENDATIONThe SAP Maintenance note was opened to inspect and fix the equipment (SAP  10909787):1. Electric motor’s winding temperature transmitter (TIT-2110A-12) should be checked. If calibration is not properly well, it should be replaced; 2. Electric motor conditions should be checked. During inspection, it was found damage electric motor´s winding transmitter. They were replaced by electric motor´s winding temperature spare.POTENTIAL SAVING ASSESSMENT$ 500.000$ 15.000WORST SCENARIOBEST SCENARIOMaintenance type: EmergencyMaintenance type: PlannedMaintenance scope: Repair the motorMaintenance scope: Replace instrument, cables, panel cardDowntime impact: No impactDowntime impact: No impactEquipment unavailability: Yes. Equipment unavailability: Yes. 
Zoom in to see it larger
Number of operationsNumber of variablesEQUIPMENT | TAGVESSEL812MV26-CM-2110A-1C (VRU)MV26
ML1

## Page 29

Slide 24
ML1 Fonte: relatório da modec
Melissa Lopes; 2023-01-10T18:55:39.385

## Page 30

Monthly reportJanuary – December 2022
Issued by Shape with the support of MODEC
CASE 21 | Abnormal readings in the electric motor bearing temperature sensorsACTION STATUS MODELLING APPROACHNOTIFICATION DATEOngoingKnowledge-based2022-12-12EVENT DESCRIPTIONThe electric motor’s bearing temperature sensors of SWIP C have been showing abnormal readings. This event was identified when thetemperature sensor presented unlikely measurements, based on environment temperature, and out of the historical data. One of thebearing temperature sensors was already under investigation for a similar problem, so we just updated the open note/deviation to checkthis other sensor (MV27-TI-1545C-32) as well.SHAPE’S APPLICATION
SPECIALIST’S RECOMMENDATIONThe SAP maintenance note was updated to check the sensors installation, calibration and its facilities (cables, connections and JB). (SAP10823771)POTENTIAL SAVING ASSESSMENT$ 1.600.000$ 250.000WORST SCENARIOBEST SCENARIOMaintenance type: EmergencyMaintenance type: PlannedMaintenance scope: Overhaul of the electric motorMaintenance scope: Replace the bearingDowntime impact: No impactDowntime impact: No impactEquipment unavailability: Yes. Equipment unavailability: Yes. 
Zoom in to see it larger
Number of operationsNumber of variablesEQUIPMENT | TAGVESSEL1418MV27-PAT-1545C-8P (SWIP)MV27
ML1

## Page 31

Slide 25
ML1 Pag 36
Melissa Lopes; 2023-01-09T18:44:41.965

## Page 32

Monthly reportJanuary – December 2022
Issued by Shape with the support of MODEC
CASE 22 | Flowmeter readings deviationACTION STATUS MODELLING APPROACHNOTIFICATION DATEOngoingKnowledge-based2022-12-01EVENT DESCRIPTIONIt was observed that the flowmeter measurement was decreasing while discharge pressure and motor current were stable. Thiscondition indicates a flowmeter deviation, because when we see the flow decreasing it means we also need the pressure to increase,which is not true in this case. And regarding the motor current, if the machine is operating with the same power level, it's not expected aflow decrease, we expect that the process condition stays steady.SHAPE’S APPLICATION
SPECIALIST’S RECOMMENDATIONPOTENTIAL SAVING ASSESSMENT$$ WORST SCENARIOBEST SCENARIOMaintenance type:EmergencyMaintenance type:PlannedMaintenance scope:Maintenance scope:Downtime impact:No impactDowntime impact:No impactEquipment unavailability:Equipment unavailability:
Zoom in to see it larger
Number of operationsNumber of variablesEQUIPMENT | TAGVESSEL23MV24-PAT-1545CMV24
ML1

## Page 33

Slide 26
ML1 Não tem no report da modec
Melissa Lopes; 2023-01-09T18:21:30.124

## Page 34

Monthly reportJanuary – December 2022
Issued by Shape with the support of MODEC
CASE 23 | Bearing temperature abnormal instrument readingsACTION STATUS MODELLING APPROACHNOTIFICATION DATEOngoingKnowledge-based2022-12-16EVENT DESCRIPTIONSystem detected a temperature increase in the Gear Shaft HS Bearing Temperature DE (MV24_TI-2210C-21), checking the trends andequipment behavior, the specialist confirmed the sensor failure event and recommended inspect and calibrate the sensor.SHAPE’S APPLICATION
SPECIALIST’S RECOMMENDATIONThe specialist confirmed the sensor failure event and recommended inspect and calibrate the sensor.POTENTIAL SAVING ASSESSMENT$$ WORST SCENARIOBEST SCENARIOMaintenance type:EmergencyMaintenance type:PlannedMaintenance scope:Maintenance scope:Downtime impact:No impactDowntime impact:No impactEquipment unavailability:Equipment unavailability:
Zoom in to see it larger
Number of operationsNumber of variablesEQUIPMENT | TAGVESSEL812MV24-CBA-2210C-3SMV24
ML1

## Page 35

Slide 27
ML1 Não tem no report da modec
Melissa Lopes; 2023-01-09T18:22:01.400

## Page 36

Monthly reportJanuary – December 2022
Issued by Shape with the support of MODEC
CASE 24 | Axial displacement abnormal instrument readingACTION STATUS MODELLING APPROACHNOTIFICATION DATEOngoingKnowledge-based2022-12-12EVENT DESCRIPTIONAxial displacement transmitter (MV26-ZI-1545B-17 and MV26-ZI-1545B-18) has shown different values between them, which are installedin same position of bearing. Their voting logic are 1oo2 type. If axial displacement transmitter shows abnormal values, it will be trigger ofunplanned stop (trip).SHAPE’S APPLICATION
SPECIALIST’S RECOMMENDATIONThe specialist recommended the following actions:1. Axial displacement transmitter position must be checked and adjusted, if applicable;2. Axial displacement transmitters must be checked and calibrated. If calibration is not available or notproperly well, the replacement must be done.POTENTIAL SAVING ASSESSMENT$ 500.000$ 30.000WORST SCENARIOBEST SCENARIOMaintenance type: EmergencyMaintenance type: PlannedMaintenance scope: Repair the pump Maintenance scope: Replace instrument, cables, panel cardDowntime impact: No impactDowntime impact: No impactEquipment unavailability: YesEquipment unavailability: Yes
Zoom in to see it larger
Number of operationsNumber of variablesEQUIPMENT | TAGVESSEL1124MV26-PAT-1545B-5PMV26
ML1

## Page 37

Slide 28
ML1 Pág 27
Melissa Lopes; 2023-01-10T13:48:23.438

## Page 38

Monthly reportJanuary – December 2022
Issued by Shape with the support of MODEC
CASE 25 | Increase of lube oil ﬁlter differential pressure ACTION STATUS MODELLING APPROACHNOTIFICATION DATEConcludedKnowledge-based2022-08-11EVENT DESCRIPTIONAfter applying the intelligence to monitor trends in the MV29 equipment through the PdM, an increase in the pressure differential in thelubricating oil filter was observed.High pressure differential in lubricating oil filters can cause oil pressure drop to the machine bearings causing low oil pressure trip.SHAPE’S APPLICATION
SPECIALIST’S RECOMMENDATIONTo avoid unwelcome trip of the equipment, it is recommended to change the lube oil filter.POTENTIAL SAVING ASSESSMENT$530.000$120.000WORST SCENARIOBEST SCENARIOMaintenance type: EmergencyMaintenance type: PlannedMaintenance scope: Repair the pumpMaintenance scope: Replace the lube oil filterDowntime impact: No impactDowntime impact: No impactEquipment unavailability: Yes. Equipment unavailability: Yes. 
Zoom in to see it larger
Number of operationsNumber of variablesEQUIPMENT | TAGVESSEL37MV29-CBA-2420A-5SMV29
ML1

## Page 39

Slide 29
ML1 Pag 38
Melissa Lopes; 2023-01-10T13:48:58.989
