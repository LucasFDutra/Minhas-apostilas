import React, {useState, useEffect} from 'react'
import axios from 'axios'
import {Redirect} from 'react-router-dom'
import {Badge} from 'reactstrap'

const InfoSerie = (props) => {
    const match = props.match
    const [form, setForm] = useState({
        name: ''
    })
    const [success, setSucces] = useState(false)
    const [mode, setMode] = useState('INFO')
    const [genres, setGenres] = useState([])
    const [genreId, setGenreId] = useState('')

    const [data, setData] = useState({})
    useEffect(() => {
        axios.get('/api/series/'+match.params.id).then(res => {
            setData(res.data)
            setForm(res.data)
        })
    }, [match.params.id])

    useEffect(()=>{
        axios.get('/api/genres').then(res=>{
            setGenres(res.data.data)
            const genres = res.data.data
            const encontrado = genres.find(value => data.genre === value.name)
            if (encontrado){
                setGenreId(encontrado.id)
            }
        })
    }, [data])


    //custom header
    const masterHeader = {
        height: '50vh', //50% do view port (tela)
        minHeight: '500px', //menor altura
        backgroundImage: `url('${data.background}')`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat'
    }

    const onChangeGenre = evt => {
        setGenreId(evt.target.value)
    }

    const onChange = (field) => (evt) => {
        setForm({
            ...form, //copia tudo que estava em form
            [field]: evt.target.value
        })
    }

    const seleciona = value => () => {
        setForm({
            ...form,
            status: value
        })
    }

    const save = () => {
        axios.put('/api/series/' + match.params.id, {
            ...form,
            genre_id: genreId
        }).then(res => {
            setSucces(true)
        })
    }
    if (success){
        return (<Redirect to='/series' />)
    }
    return(
        <div>
            <header style={masterHeader}>
                <div className='h-100' style={{background: 'rgba(0,0,0,0.7)'}}>
                    <div className='h-100 container'>
                        <div className='row h-100 align-items-center'> {/* uma row é divida em 12 partes*/}
                            <div className='col-3'> {/* o col 3 pega 3/12 partes dessa linha*/}
                                <img alt={data.name} className='img-fluid img-thumbnail' src={data.poster} />
                            </div>
                            <div className='col-8'>
                                <h1 className='font-weight-light text-white'>{data.name}</h1>
                                <div className='lead text-white'>
                                    {data.status==='ASSISTIDO' && <Badge color='success' style={{margin: '5px'}}>Assistido</Badge>}
                                    {data.status==='PARA_ASSISTIR' && <Badge color='warning' style={{margin: '5px'}}>Para assistir</Badge>}
                                    <Badge color='primary' style={{margin: '5px'}}>{data.genre}</Badge>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </header>
            <div className='container'>
                <button className='btn btn-primary' style={{margin: '5px'}} onClick={() => setMode('EDIT')}>Editar</button>
            </div>
            {
                mode === 'EDIT' && //se não estiver no modo de edição ele não mostra nada que está abaixo
                <div className='container'>
                    <h1>Informações</h1>
                    <button className='btn btn-primary' style={{margin: '5px'}} onClick={() => setMode('INFO')}>Cancelar</button>
                    <form>
                        <div className="form-group">
                            <label htmlFor="name">Nome da Série</label>
                            <input type="text" value={form.name} onChange={onChange('name')} className="form-control" id="name" placeholder="Nome da Série" />
                        </div>
                        <div className="form-group">
                            <label htmlFor="name">Comentários</label>
                            <input type="text" value={form.comments} onChange={onChange('comments')} className="form-control" id="comments" placeholder="Deixe seu comentário" />
                        </div>
                        <div className="form-group">
                            <label htmlFor="genres">Genêro</label>
                            <select className="form-control" onChange={onChangeGenre} value={genreId}>
                                {genres.map(genre => <option key={genre.id} value={genre.id}>{genre.name}</option>)}
                            </select>
                        </div>
                        <div className="form-check">
                            <input className="form-check-input" type="radio" checked={form.status === 'ASSISTIDO'} name="status" id="assistido" value="ASSISTIDO" onChange={seleciona('ASSISTIDO')}/>
                            <label className="form-check-label" htmlFor="assitido">
                                Assistido
                            </label>
                        </div>
                        <div className="form-check">
                            <input className="form-check-input" type="radio" checked={form.status === 'PARA_ASSISTIR'} name="status" id="paraAssitir" value="PARA_ASSISTIR" onChange={seleciona('PARA_ASSISTIR')}/>
                            <label className="form-check-label" htmlFor="paraAssistir">
                                Para Assistir
                            </label>
                        </div>
                        <button type="button" onClick={save} className="btn btn-primary" style={{margin: '5px'}}>Salvar</button>
                    </form>
                </div>
            }
        </div>
    )
}

export default InfoSerie