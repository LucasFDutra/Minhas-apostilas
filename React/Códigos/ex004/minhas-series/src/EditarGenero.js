import React, {useState, useEffect} from 'react'
import axios from 'axios'
import {Redirect} from 'react-router-dom'

const EditarGenero = (props) => {
    const match = props.match // poderia utilizar outro método para fazer isso.
    const [name, setName] = useState('')
    const [success, setSucces] = useState(false)

    useEffect(() => {
        axios.get('/api/genres/'+match.params.id).then(res => {
            setName(res.data.name)
        })
    }, [match.params.id])

    const onChange = (evt) => {
        setName(evt.target.value)
    }
    const save = () => {
        axios.put('/api/genres/'+match.params.id, {
            name: name
        }).then(res => {
            setSucces(true)
        })
    }
    if (success){
        return (<Redirect to='/generos' />)
    }
    return(
        <div className='container'>
            <h1>Editar Genêro</h1>
            <form>
                <div className="form-group">
                    <label htmlFor="name">Nome do Genêro</label>
                    <input type="text" value={name} onChange={onChange} className="form-control" id="name" placeholder="Nome do Gênero" />
                </div>
                <button type="button" onClick={save} className="btn btn-primary">Salvar</button>
            </form>
        </div>
    )
}

export default EditarGenero