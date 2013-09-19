
#import pyNN
from pyNN.lemslite import *


#setup()
#population1  = Population(5, LEMSLightModel(xmlcomponentname='comp1.xml'), label="input")
#population2  = Population(250, LEMSLightModel(xmlcomponentname='comp2.xml'), label="dINs")
#population3  = Population(1500, LEMSLightModel(xmlcomponentname='comp3.xml'), label="Non-dINs")
#
#ass1 = population1 + population2
#ass2 = population2[30:50] + population3[30:50]
#
#projection1 = EventProjection(ass1, ass2,
#                        AllToAllConnector(),
#                        delay = 'fixed:2e-3',
#                        src_portname="on_emit_event",
#                        dst_portname="on_recv_ampa_event",
#                        portmap = {
#                                #dst-param:    #src-port
#                                'weight':      'src-param:weight',
#                                }
#                        )
#
#projection2 = EventProjection(population1, ass2,
#                        FromListConnector([(0,1), (4,3)]),
#                        delay = 'fixed:3e-3',
#                        src_portname="on_emit_event",
#                        dst_portname="on_recv_ampa_event",
#                        portmap = {
#                                #dst-param:    #src-port
#                                'weight':      'fixed:1.0',
#                        })
#
#projection3 = AnalogProjection(population1, ass2,
#                        FixedProbabilityConnector(0.2),
#                        joining_component='gap_junction',
#                        src_portname="on_emit_event",
#                        dst_portname="on_recv_ampa_event",
#                        portmap = {
#                            #dst-param:    #src-port
#                            'joining_component:V1':      'pop1:V',
#                            'joining_component:V2':      'pop2:V',
#                            'joining_component:i1':      'pop1:i_inj',
#                            'joining_component:i2':      'pop2:i_inj',
#                        })
#
#write_xml()





setup()
rb_input  = Population(5, LEMSLightModel(xmlcomponentname='rb_spike_gen.xml'), label="input")
dINs  = Population(236, LEMSLightModel(xmlcomponentname='din.xml'), label="dINs")
non_dINs  = Population(1146, LEMSLightModel(xmlcomponentname='non_din.xml'), label="Non-dINs")


LHS_MN  = non_dINs[ 0   : 0+169]
LHS_RB  = non_dINs[ 169 : 169+63]
LHS_aIN = non_dINs[ 232 : 232+68]
LHS_cIN = non_dINs[ 300 : 300+192]
LHS_dla = non_dINs[ 492 : 492+29]
LHS_dlc = non_dINs[ 521 : 521+52]
RHS_MN  = non_dINs[ 573 : 573+169]
RHS_RB  = non_dINs[ 742 : 742+63]
RHS_aIN = non_dINs[ 805 : 805+68]
RHS_cIN = non_dINs[ 873 : 873+192]
RHS_dla = non_dINs[ 1065: 1065+29]
RHS_dlc = non_dINs[ 1094: 1094+52]

LHS_dIN = dINs[ 0: 118]
RHS_dIN = dINs[ 118: 236]

LHS_hdIN = dINs[0:50]
RHS_hdIN = dINs[0+118:50+118]


# Connect input to RB cells:
projection1 = EventProjection(rb_input, LHS_RB, FromListConnector([]), delay = 'fixed:2e-3',
                        src_portname="on_emit_event",
                        dst_portname="on_recv_ampa_event", portmap = {'weight': 'fixed:10.0' })


#| ('NondINs', 'NondINs', ('ampa', 0.593)) |  1175 |
projection1 = EventProjection(non_dINs, non_dINs, FromListConnector([]), delay = 'fixed:2e-3',
                        src_portname="on_emit_event", label= "non_dINs->non_dINs (ampa)",
                        dst_portname="on_recv_ampa_event", portmap = {'weight': 'fixed:0.593' })

#|  ('NondINs', 'NondINs', ('ampa', 8.0))  |  5355 |
projection1 = EventProjection(non_dINs, non_dINs, FromListConnector([]), delay = 'fixed:2e-3',
                        src_portname="on_emit_event", label= "non_dINs->non_dINs (ampa)",
                        dst_portname="on_recv_ampa_event", portmap = {'weight': 'fixed:8.0' })

#|  ('NondINs', 'NondINs', ('inh', 0.435)) | 36068 |
projection1 = EventProjection(non_dINs, non_dINs, FromListConnector([]), delay = 'fixed:2e-3',
                        src_portname="on_emit_event", label= "non_dINs->non_dINs (inh)",
                        dst_portname="on_recv_inh_event", portmap = {'weight': 'fixed:0.435' })

#|  ('NondINs', 'NondINs', ('nmda', 0.29)) | 13591 |
projection1 = EventProjection(non_dINs, non_dINs, FromListConnector([]), delay = 'fixed:2e-3',
                        src_portname="on_emit_event", label= "non_dINs->non_dINs (nmda)",
                        dst_portname="on_recv_nmda_event", portmap = {'weight': 'fixed:0.29' })


#|   ('NondINs', 'dINs', ('ampa', 0.593))  |  208  |
projection1 = EventProjection(non_dINs, dINs, FromListConnector([]), delay = 'fixed:2e-3',
                        src_portname="on_emit_event", label= "non_dINs->dINs (ampa)",
                        dst_portname="on_recv_ampa_event", portmap = {'weight': 'fixed:0.593' })
#|   ('NondINs', 'dINs', ('inh', 0.435))   |  8065 |
projection1 = EventProjection(non_dINs, dINs, FromListConnector([]), delay = 'fixed:2e-3',
                        src_portname="on_emit_event", label= "non_dINs->dINs (inh)",
                        dst_portname="on_recv_inh_event", portmap = {'weight': 'fixed:0.435' })
#|   ('NondINs', 'dINs', ('nmda', 0.29))   |  1479 |
projection1 = EventProjection(non_dINs, dINs, FromListConnector([]), delay = 'fixed:2e-3',
                        src_portname="on_emit_event", label= "non_dINs->dINs (nmda)",
                        dst_portname="on_recv_nmda_event", portmap = {'weight': 'fixed:0.29' })
#|    ('NondINs', 'dINs', ('nmda', 1.0))   |  1937 |
projection1 = EventProjection(non_dINs, dINs, FromListConnector([]), delay = 'fixed:2e-3',
                        src_portname="on_emit_event", label= "non_dINs->dINs (nmda)",
                        dst_portname="on_recv_nmda_event", portmap = {'weight': 'fixed:1.0' })


#|    ('dINs', 'NondINs', ('ampa', 0.1))   |  3364 |
projection1 = EventProjection(dINs, non_dINs, FromListConnector([]), delay = 'fixed:2e-3',
                        src_portname="on_emit_event", label= "dINs->non_dINs (ampa)",
                        dst_portname="on_recv_ampa_event", portmap = {'weight': 'fixed:0.1' })
#|   ('dINs', 'NondINs', ('ampa', 0.593))  | 13099 |
projection1 = EventProjection(dINs, non_dINs, FromListConnector([]), delay = 'fixed:2e-3',
                        src_portname="on_emit_event", label= "dINs->non_dINs (ampa)",
                        dst_portname="on_recv_ampa_event", portmap = {'weight': 'fixed:0.593' })
#|    ('dINs', 'dINs', ('ampa', 0.593))    |  4103 |
projection1 = EventProjection(dINs, non_dINs, FromListConnector([]), delay = 'fixed:2e-3',
                        src_portname="on_emit_event", label= "dINs->non_dINs (ampa)",
                        dst_portname="on_recv_ampa_event", portmap = {'weight': 'fixed:0.593' })
#|     ('dINs', 'dINs', ('nmda', 0.15))    |  4103 |
projection1 = EventProjection(dINs, non_dINs, FromListConnector([]), delay = 'fixed:2e-3',
                        src_portname="on_emit_event", label= "dINs->non_dINs (nmda)",
                        dst_portname="on_recv_nmda_event", portmap = {'weight': 'fixed:0.15' })


# Gap junctions:
projection3 = AnalogProjection(LHS_hdIN,LHS_hdIN,
                        FixedProbabilityConnector(0.2),
                        joining_component='gap_junction.xml',
                        portmap = {
                            #dst-param:    #src-port
                            'joining_component:V1':      'pop1:V',
                            'joining_component:V2':      'pop2:V',
                            'joining_component:i1':      'pop1:i_inj',
                            'joining_component:i2':      'pop2:i_inj',
                        })

projection3 = AnalogProjection(RHS_hdIN,RHS_hdIN,
                        FixedProbabilityConnector(0.2),
                        joining_component='gap_junction.xml',
                        portmap = {
                            #dst-param:    #src-port
                            'joining_component:V1':      'pop1:V',
                            'joining_component:V2':      'pop2:V',
                            'joining_component:i1':      'pop1:i_inj',
                            'joining_component:i2':      'pop2:i_inj',
                        })



#
#projection2 = EventProjection(population1, ass2,
#                        FromListConnector([(0,1), (4,3)]),
#                        delay = 'fixed:3e-3',
#                        src_portname="on_emit_event",
#                        dst_portname="on_recv_ampa_event",
#                        portmap = {
#                                #dst-param:    #src-port
#                                'weight':      'fixed:1.0',
#                        })
#


#
xml = write_xml()

with open('testout1.xml','w') as f:
    f.write(xml)





