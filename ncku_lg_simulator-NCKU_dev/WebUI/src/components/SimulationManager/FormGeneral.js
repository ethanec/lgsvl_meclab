/**
 * Copyright (c) 2019 LG Electronics, Inc.
 *
 * This software contains code licensed as described in LICENSE.
 *
 */

import React, {useState, useEffect, useContext, useCallback} from 'react';
import SingleSelect from '../Select/SingleSelect';
import Alert from '../Alert/Alert';
import Checkbox from '../Checkbox/Checkbox';
import appCss from '../../App/App.module.less';
import {getList} from '../../APIs.js'
import {IoIosClose} from "react-icons/io";
import { SimulationContext } from "../../App/SimulationContext";
import axios from 'axios';

function FormGeneral() {
    const [clusterList, setClusterList] = useState();
    const [alert, setAlert] = useState({status: false});
    const [simulation, setSimulation] = useContext(SimulationContext);
    const {name, cluster, apiOnly, headless, interactive} = simulation;
    const changeName = useCallback(ev => setSimulation({...simulation, name: ev.target.value}));
    const changeApiOnly = useCallback(() => setSimulation(prev => ({...simulation, apiOnly: !prev.apiOnly})));
    const changeHeadless = useCallback(() => setSimulation(prev => ({...simulation, headless: !prev.headless})));
    const changeCluster = useCallback(ev => setSimulation({...simulation, cluster: parseInt(ev.target.value)}));
    let source = axios.CancelToken.source();
    let unmounted;
    useEffect(() => {
        unmounted = false;
        const fetchData = async () => {
            setAlert({status: false});
            const result = await getList('clusters', source.token);
            if (unmounted) return;
            if (result.status === 200) {
                setClusterList(result.data);
                if (!result.data.filter(c => c.id === cluster).length)
                {
                    // Reset cluster to default
                    setSimulation({...simulation, cluster: 0});
                }

            } else {
                let alertMsg;
                if (result.name === "Error") {
                    alertMsg = result.message;
                } else {
                    alertMsg = `${result.statusText}: ${result.data.error}`;
                }
                setAlert({status: true, type: 'error', message: alertMsg});
            }
        };

        fetchData();
        return () => {
            unmounted = true;
            source.cancel('Cancelling in cleanup.')
        };
    }, []);

    function alertHide () {
        setAlert({status: false});
    }

    return (
        <div className={appCss.formCard}>
            {
                alert.status &&
                <Alert type={alert.alertType} msg={alert.alertMsg}>
                    <IoIosClose onClick={alertHide} />
                </Alert>
            }
            <h4 className={appCss.inputLabel}>
                Simulation Name
            </h4>
            <input
                required
                name="name"
                type="text"
                defaultValue={name}
                placeholder="name"
                onChange={changeName} />
            <br />
            <br />
            <h4 className={appCss.inputLabel}>
                Select Cluster
            </h4>
            <p className={appCss.inputDescription}>
                Select cluster to run distributed simulation on several machines.
            </p>
            <SingleSelect
                data-for='cluster'
                placeholder='select a cluster'
                defaultValue={cluster}
                onChange={changeCluster}
                options={clusterList}
                label="name"
                value="id"
            />
            <br />
            <br />
            <h4 className={appCss.inputLabel}>
                API Only
            </h4>
            <p className={appCss.inputDescription}>
                Simulation in API only mode is fully controlled by Python API. Map, Ego Vehicle and other parameters are defuned using API.
            </p>
            <Checkbox
                checked={apiOnly}
                label="Use API to control simulation"
                name={'apiOnly'}
                onChange={changeApiOnly}/>
            <br />
            <h4 className={appCss.inputLabel}>
                Headless Mode
            </h4>
            <p className={appCss.inputDescription}>
                In Headless Mode main view is not rendered. Use this mode to optimize simulation performance when interaction is not needed.
            </p>
            <Checkbox
                checked={headless}
                label="Run simulation in Headless Mode"
                name={'headless'}
                disabled={interactive}
                onChange={changeHeadless} />
            </div>
        )
}

export default FormGeneral;